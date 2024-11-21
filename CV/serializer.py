from rest_framework import serializers
from .models import *


class cvserializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'


class experienceserializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
class diplomaserializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = '__all__'
