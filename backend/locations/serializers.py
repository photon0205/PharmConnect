from rest_framework import serializers
from .models import UserLocation
from accounts.models import User

class UserLocationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserLocation
        fields = ('id', 'user', 'latitude', 'longitude', 'created_at')