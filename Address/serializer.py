from rest_framework import serializers
from .models import *


class addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
