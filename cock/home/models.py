

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_field = models.CharField(max_length=255)  # Add your custom field(s) here

    def __str__(self):
        return self.user.username
    
