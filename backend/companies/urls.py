from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.StoresAPIView.as_view(), name='all-stores-of-company'),
    path('stores/inventory/', views.StoreInventory.as_view(), name='store-inventory'),
    path('sorted/', views.AllStoresSortedByLocation.as_view(), name='all-stores-sorted-by-location'),
    path('stores/<int:store_id>/', views.StoreDetailAPIView.as_view(), name='store_detail'),
    path('stores/<int:store_id>/manager/', views.UpdateStoreManager.as_view(), name='update_store_manager'),
    path('products/', views.ProductAPIView.as_view(), name='product_api'),
    path('stores/<int:store_id>/stats/', views.StatisticsAPIView.as_view(), name='store_statistics_api'),
    path('products/search/', views.ProductSearchAPIView.as_view(), name='product_search'),
]
