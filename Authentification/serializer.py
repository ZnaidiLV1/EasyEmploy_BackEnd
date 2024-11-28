from rest_framework import serializers
from .models import CustomUser, Address
from Address.serializer import addressSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # Accept 'city' and 'country' as part of the incoming data
    city = serializers.CharField(write_only=True)
    country = serializers.CharField(write_only=True)
    address = addressSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'email', 'password', 'user_image', 'role',
            'first_name', 'last_name', 'age_user', 'num_tlfn',
            'name', 'ref_entreprise', 'city', 'country', 'verification_code','address'
        ]

    def create(self, validated_data):
        # Extract city and country from the validated data
        city = validated_data.pop('city')
        country = validated_data.pop('country')

        # Create the Address instance
        address_instance = Address.objects.create(city=city, country=country)

        # Create the CustomUser instance and associate the address instance
        user = CustomUser.objects.create(address=address_instance, **validated_data)

        # Set the password securely
        password = validated_data.pop('password', None)
        if password:
            user.set_password(password)

        user.save()
        return user
