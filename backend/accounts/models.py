from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    USER_ROLES = (
        ('CEO', 'CEO'),
        ('STORE_MANAGER', 'Store Manager'),
        ('USER', 'User'),
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='USER')
    address = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    objects = CustomUserManager()

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100, unique=True)
    store = models.ForeignKey('companies.Store', on_delete=models.CASCADE, related_name='workers')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name