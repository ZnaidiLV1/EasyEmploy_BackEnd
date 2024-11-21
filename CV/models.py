from django.db import models
from Authentification.models import CustomUser
class CV(models.Model):
    client_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    professional_level=models.CharField(default="")
    salary=models.IntegerField(default=0)
    bio=models.CharField(default="")
    git_link=models.CharField(blank=True,null=True)
    linkedIn_link=models.CharField(blank=True,null=True)
    x_link=models.CharField(blank=True,null=True)
    portfolio_link=models.CharField(blank=True,null=True)
    soft_life_description=models.CharField(max_length=255)

class Experience(models.Model):
    cv_id=models.ForeignKey(CV,on_delete=models.CASCADE)
    titre=models.CharField(max_length=255)
    lieu=models.CharField(max_length=255)
    date_debut=models.DateField()
    date_fin=models.DateField()
    description=models.CharField(max_length=255)

class Diploma(models.Model):
    cv_id=models.ForeignKey(CV,on_delete=models.CASCADE)
    titre=models.CharField(max_length=255)
    university=models.CharField(max_length=255)
    date_debut=models.DateField()
    date_fin=models.DateField()
    current=models.BooleanField()


# Create your models here.
