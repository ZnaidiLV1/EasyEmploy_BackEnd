from django.db import models

from CV.models import CV
from CompanyCard.models import CompanyCard


class Fields(models.Model):
    name = models.CharField()

class CvPerField(models.Model):
    field_id = models.ForeignKey(Fields, on_delete=models.CASCADE)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE)

class CompanyCardPerField(models.Model):
    companyCard_id=models.ForeignKey(CompanyCard,on_delete=models.CASCADE)
    field_id=models.ForeignKey(Fields,on_delete=models.CASCADE)

# Create your models here.
