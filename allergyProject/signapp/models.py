from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=30)