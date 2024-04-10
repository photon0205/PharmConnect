from rest_framework import serializers
from .models import Product, Inventory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'product', 'store', 'quantity')