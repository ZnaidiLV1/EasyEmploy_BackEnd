from django.db import models

from CV.models import CV


class Fields(models.Model):
    name = models.CharField()

class CvPerField(models.Model):
    field_id = models.ForeignKey(Fields, on_delete=models.CASCADE)
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE)

# Create your models here.
