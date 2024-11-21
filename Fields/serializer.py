from rest_framework import serializers
from .models import *


class fieldserializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = '__all__'

class cvPerFieldserializer(serializers.ModelSerializer):
    class Meta:
        model = CvPerField
        fields = '__all__'