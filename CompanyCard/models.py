from django.db import models

from Authentification.models import CustomUser


class CompanyCard(models.Model):
    user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    street=models.CharField()
    size=models.IntegerField()
    bio=models.CharField()
    employees_number=models.IntegerField()
    establishment_date=models.DateTimeField()
    git_link=models.CharField(blank=True, null=True)
    linkedIn_link=models.CharField(blank=True, null=True)
    x_link=models.CharField(blank=True, null=True)
    website_link=models.CharField(blank=True, null=True)

# Create your models here.
