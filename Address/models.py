from django.db import models
from Authentification.models import CustomUser
class Address(models.Model):
    user_address=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    country=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    street=models.CharField(max_length=255)

# Create your models here.
