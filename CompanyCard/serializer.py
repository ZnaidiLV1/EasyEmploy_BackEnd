from rest_framework import serializers

from CompanyCard.models import CompanyCard


class companyCardserializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCard
        fields = '__all__'
