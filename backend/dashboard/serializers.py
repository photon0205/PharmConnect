from rest_framework import serializers
from accounts.models import User
from orders.models import Order

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'store', 'status', 'created_at')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')