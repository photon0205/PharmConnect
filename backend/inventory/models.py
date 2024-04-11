from django.contrib.gis.db import models
from companies.models import Store

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.store.name}"