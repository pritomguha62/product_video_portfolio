from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.

class CustomAdmin(AbstractUser):
    username = None
    
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    user_bio = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="profile_image")
    face_image = models.ImageField(upload_to="face_image")
    # user_type = models.CharField(max_length=10, choices=(('admin', 'Admin'), ('staff', 'Staff'), ('user', 'User')), default='user') 
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []

