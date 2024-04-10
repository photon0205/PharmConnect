from django.db import models
from accounts.models import User

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Location"
