from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import IsCEO, IsStoreManager
from .models import Company, Store, Inventory, Product
from .serializers import ProductSerializer, StoreSerializer, InventorySerializer
from accounts.models import User
from math import radians, sin, cos, sqrt, atan2

class StoresAPIView(APIView):
    permission_classes = [IsCEO]

    def get(self, request):
        try:
            company = request.user.companies.first()
            stores = Store.objects.filter(company=company)
            serializer = StoreSerializer(stores, many=True)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response(
                {"message": "Company not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        company_id = Company.objects.filter(ceo=request.user).first().id
        request.data["company"] = company_id
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            manager_id = request.data.get("manager_id")
            serializer.validated_data["manager_id"] = manager_id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetailAPIView(APIView):
    permission_classes = [IsCEO | IsStoreManager]

    def get_object(self, store_id):
        try:
            return Store.objects.get(id=store_id)
        except Store.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, store_id):
        store = self.get_object(store_id)
        serializer = StoreSerializer(store)
        serialized_data=[]
        serialized_data.append(serializer.data)
        stats_response = self.get_store_statistics(store_id)
        if stats_response.status_code == status.HTTP_200_OK:
            store_statistics = stats_response.data
            serialized_data[0]['statistics'] = store_statistics
        
        products = Product.objects.filter(store=store)
        serialized_products = []

        for product in products:
            serialized_product = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'total_sold_quantity': product.total_sold_quantity,
                'store': product.store_id,
            }

            inventory = product.inventory.first()
            available_quantity = inventory.quantity if inventory else 0
            serialized_product['available_quantity'] = available_quantity

            serialized_products.append(serialized_product)
        serialized_data[0]['products'] = serialized_products
        return Response(serialized_data)

    def put(self, request, store_id):
        store = self.get_object(store_id)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, store_id):
        store = self.get_object(store_id)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_store_statistics(self, store_id):
        try:
            store = Store.objects.get(id=store_id)
            total_products = Product.objects.filter(store=store).count()
            low_stock_product = (
                Product.objects.filter(store=store)
                .order_by("-inventory__quantity")
                .last()
            )
            top_selling_product = (
                Product.objects.filter(store=store)
                .order_by("-total_sold_quantity")
                .first()
            )

            if top_selling_product:
                top_selling_product_name = top_selling_product.name
                top_selling_product_qty = top_selling_product.total_sold_quantity
                top_selling_product_revenue = (
                    top_selling_product.total_sold_quantity * top_selling_product.price
                )
            else:
                top_selling_product_name = None
                top_selling_product_qty = None
                top_selling_product_revenue = None

            statistics = {
                "total_products": total_products,
                "top_selling_product": {
                    "name": top_selling_product_name,
                    "quantity_sold": top_selling_product_qty,
                    "total_revenue": top_selling_product_revenue,
                },
                 "low_stock_product": {
                    "name": low_stock_product.name,
                    "current_quantity": sum(
                        inventory.quantity
                        for inventory in low_stock_product.inventory.all()
                    ),
                },
            }

            return Response(statistics, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UpdateStoreManager(APIView):
    permission_classes = [IsCEO]

    def put(self, request, store_id):
        try:
            store = Store.objects.get(id=store_id)
            new_manager_id = request.data.get("manager_id")
            new_manager, created = User.objects.get_or_create(
                id=new_manager_id,
                defaults={"password": User.objects.make_random_password()},
            )
            if created:
                new_manager.save()
            store.manager = new_manager
            store.save()
            return Response(
                {
                    "message": "Store manager updated successfully",
                    "new_manager_password": new_manager.password,
                },
                status=status.HTTP_200_OK,
            )
        except Store.DoesNotExist:
            return Response(
                {"message": "Store not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except User.DoesNotExist:
            return Response(
                {"message": "Manager not found"}, status=status.HTTP_404_NOT_FOUND
            )


class StoreInventory(APIView):
    permission_classes = [IsStoreManager]

    def get(self, request):
        try:
            store = request.user.stores.first()
            inventory = Inventory.objects.filter(store=store)
            serializer = InventorySerializer(inventory, many=True)
            return Response(serializer.data)
        except Store.DoesNotExist:
            return Response(
                {"message": "Store not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request):
        try:
            store = request.user.stores.first()
            product_id = request.data.get("product_id")
            quantity = int(request.data.get("quantity", 0))
            action = request.data.get("action")
            product = Product.objects.get(id=product_id)

            inventory, created = Inventory.objects.get_or_create(
                store=store, product=product
            )

            if action == "add":
                inventory.quantity += quantity
            elif action == "remove":
                inventory.quantity -= quantity

            inventory.save()

            return Response(
                {"message": "Inventory updated successfully"}, status=status.HTTP_200_OK
            )
        except Store.DoesNotExist:
            return Response(
                {"message": "Store not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )


class AllStoresSortedByLocation(APIView):
    def get(self, request):
        try:
            latitude = float(request.query_params.get("latitude"))
            longitude = float(request.query_params.get("longitude"))
            stores = Store.objects.all().order_by("latitude", "longitude")
            serializer = StoreSerializer(stores, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(
                {"message": "Invalid latitude or longitude"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class SearchProductByName(APIView):
    def get(self, request):
        product_name = request.query_params.get("name", "")
        products = Product.objects.filter(name__icontains=product_name)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductAPIView(APIView):
    def get(self, request):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        if latitude and longitude:
            user_lat = radians(float(latitude))
            user_lon = radians(float(longitude))
            products = Product.objects.all()

            for product in products:
                store_lat = radians(product.store.latitude)
                store_lon = radians(product.store.longitude)

                dlon = store_lon - user_lon
                dlat = store_lat - user_lat
                a = sin(dlat / 2)**2 + cos(user_lat) * cos(store_lat) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                distance = 6371 * c
                product.distance = distance

            products = sorted(products, key=lambda x: x.distance)
        else:
            products = Product.objects.all()

        # Serialize and return sorted products
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data)

    def post(self, request):
        permission_classes = [IsStoreManager | IsCEO]

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StatisticsAPIView(APIView):
    permission_classes = [IsCEO]

    def get(self, request, store_id):
        try:
            company = request.user.companies.first()
            store = Store.objects.get(id=store_id, company=company)
            
            total_products = Product.objects.filter(store=store).count()
            low_stock_product = (
                Product.objects.filter(store=store)
                .order_by("-inventory__quantity")
                .last()
            )
            top_selling_product = (
                Product.objects.filter(store=store)
                .order_by("-total_sold_quantity")
                .first()
            )

            if top_selling_product:
                top_selling_product_name = top_selling_product.name
                top_selling_product_qty = top_selling_product.total_sold_quantity
                top_selling_product_revenue = (
                    top_selling_product.total_sold_quantity * top_selling_product.price
                )
            else:
                top_selling_product_name = None
                top_selling_product_qty = None
                top_selling_product_revenue = None

            statistics = {
                "total_products": total_products,
                "top_selling_product": {
                    "name": top_selling_product_name,
                    "quantity_sold": top_selling_product_qty,
                    "total_revenue": top_selling_product_revenue,
                },
                "low_stock_product": {
                    "name": low_stock_product.name if low_stock_product else None,
                    "current_quantity": low_stock_product.inventory.quantity if low_stock_product else None,
                },
            }

            return Response(statistics)
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ProductSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        if query:
            products = Product.objects.filter(name__icontains=query)
            serialized_products = ProductSerializer(products, many=True)
            return Response(serialized_products.data)
        else:
            return Response({'message': 'Query parameter "query" is required'}, status=status.HTTP_400_BAD_REQUEST)

