from django.contrib import admin
from .models import UserLocation

@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'latitude', 'longitude', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)