from django.contrib import admin
from .models import Company, Store

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'ceo')
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'manager', 'latitude', 'longitude')
    search_fields = ('name', 'company__name')
    list_filter = ('company',)
    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'manager')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude')
        }),
    )