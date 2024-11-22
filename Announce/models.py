from django.db import models
from Authentification.models import CustomUser
from Skills.models import Skill


class Announce(models.Model):
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    required_level=models.CharField(default="")
    position_type=models.CharField(default="")
    date_publication=models.DateField(auto_now=True)
    contenu=models.CharField(max_length=255,null=True)
    is_checked= models.BooleanField(default=True)
    places_disponibles=models.IntegerField()
    type_announce=models.BooleanField(default=False)
    address=models.CharField(default="")

class AnnouncePerUser(models.Model):
    announce_id=models.ForeignKey(Announce,on_delete=models.CASCADE)
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date_postule=models.DateField(auto_now=True)

class SkillPerAnnounce(models.Model):
    announce_id = models.ForeignKey(Announce, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

# Create your models here.
