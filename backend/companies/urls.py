from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
    path('stores/', views.StoreListCreateView.as_view(), name='store-list-create'),
    path('stores/<int:pk>/', views.StoreRetrieveUpdateDestroyView.as_view(), name='store-detail'),
    path('stores/<int:store_id>/managers/', views.StoreManagerListCreateView.as_view(), name='store-manager-list-create'),
    path('stores/<int:store_id>/managers/<int:pk>/', views.StoreManagerRetrieveUpdateDestroyView.as_view(), name='store-manager-detail'),
]