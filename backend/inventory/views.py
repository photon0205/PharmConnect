from rest_framework import generics, permissions
from .models import Product, Inventory
from .serializers import ProductSerializer, InventorySerializer

class ProductListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer
    
    def get(self, request):
        name = request.query_params.get('name')
        products = Product.objects.filter(name__iexact=name)
        serializer = self.serializer_class(products, many=True)
        return serializer.data

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class InventoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer