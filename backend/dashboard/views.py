from rest_framework import generics, permissions
from orders.models import Order
from .serializers import DashboardSerializer, OrderHistorySerializer, ProfileSerializer

class DashboardView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DashboardSerializer

    def get_object(self):
        return self.request.user

class OrderHistoryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderHistorySerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user