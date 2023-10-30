from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True, max_length=50)
    avatar = CloudinaryField('image', default='placeholder')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    region = models.CharField(blank=True, max_length=50)
    occupation = models.CharField(blank=True, max_length=50)


    def __str__(self):
        return self.user.username


class Contact(models.Model):
    """
    Model for feedback messages 
    """
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=1000)


    def __str__(self):
        return self.name
