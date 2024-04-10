from rest_framework import generics, permissions
from .models import Product, Inventory
from .serializers import ProductSerializer, InventorySerializer

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