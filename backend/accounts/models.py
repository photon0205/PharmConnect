from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('CEO', 'CEO'),
        ('STORE_MANAGER', 'Store Manager'),
        ('USER', 'User'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES, default='USER')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_set',
        related_query_name='accounts_user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_set',
        related_query_name='accounts_user',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )