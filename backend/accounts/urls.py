from django.urls import path
from .views import (
    UserRegisterAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    WorkerListCreateAPIView,
    WorkerDetailAPIView,
)

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout"),
    path("workers/", WorkerListCreateAPIView.as_view(), name="worker-list-create"),
    path("workers/<int:pk>/", WorkerDetailAPIView.as_view(), name="worker-detail"),
]
