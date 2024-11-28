from django.db import models
class Address(models.Model):
    country=models.CharField(max_length=255)
    city=models.CharField(max_length=255)

# Create your models here.
