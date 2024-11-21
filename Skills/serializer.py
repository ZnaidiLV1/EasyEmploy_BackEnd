from rest_framework import serializers
from .models import *


class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class spcSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillPerCv
        fields = '__all__'
