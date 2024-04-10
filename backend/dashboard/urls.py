from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('order-history/', views.OrderHistoryView.as_view(), name='order-history'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]