from rest_framework import serializers
from .models import Inventory, Store, Product

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("id", "product", "quantity")

class StoreSerializer(serializers.ModelSerializer):
    manager_name = serializers.SerializerMethodField()
    inventory = InventorySerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = (
            "id",
            "name",
            "company",
            "manager_id",
            "manager_name",
            "longitude",
            "latitude",
            "inventory",
        )

    def get_manager_name(self, obj):
        manager = obj.manager
        if manager:
            return manager.get_full_name()  # Assuming User model has get_full_name() method
        return None

class ProductSerializer(serializers.ModelSerializer):
    store_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "store", "store_name", "total_sold_quantity", "image_url")

    def get_store_name(self, obj):
        store = obj.store
        if store:
            return store.name
        return None
