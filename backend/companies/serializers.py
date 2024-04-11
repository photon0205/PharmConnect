from rest_framework import serializers
from .models import Company, Store
from accounts.models import User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'ceo')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'company', 'manager', 'location')

class StoreManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')