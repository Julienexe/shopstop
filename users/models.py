from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from .managers import CustomUserManager

#the custom user model
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, blank=True) 
    contact = models.CharField( max_length= 50, default = '+256755565556')
    name = models.CharField(max_length = 255, default= 'user')

    def __str__(self):
        return f'{self.user.email} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)
