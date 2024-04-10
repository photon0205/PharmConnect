from django.contrib import admin
from .models import Product, Inventory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'quantity')
    search_fields = ('product__name', 'store__name')
    list_filter = ('store',)