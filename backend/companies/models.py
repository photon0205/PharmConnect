from django.db import models
from accounts.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='stores')
    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stores',
        limit_choices_to={'role': 'STORE_MANAGER'}
    )
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
