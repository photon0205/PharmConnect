from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('user-locations/', views.UserLocationListCreateView.as_view(), name='user-location-list-create'),
    path('user-locations/<int:pk>/', views.UserLocationRetrieveUpdateDestroyView.as_view(), name='user-location-detail'),
]