from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')
    username = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.first_name
    
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.username

