from django.db import models
from CV.models import CV
class Skill(models.Model):
    name=models.CharField(max_length=255)

class SkillPerCv(models.Model):
    cv_id = models.ForeignKey(CV, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

# Create your models here.
