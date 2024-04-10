from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('inventory/', views.InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', views.InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),
]