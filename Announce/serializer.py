from rest_framework import serializers
from .models import *


class announceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announce
        fields = "__all__"


class announcePerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncePerUser
        fields = "__all__"


class spaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillPerAnnounce
        fields = "__all__"
