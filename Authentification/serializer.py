from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password should be write-only

    class Meta:
        model = CustomUser
        fields = [
            'email', 'password', 'user_image', 'role',
            'first_name', 'last_name', 'age_user', 'num_tlfn', 'name',
            'ref_entreprise'
        ]

    def create(self, validated_data):
        # Remove password from validated data
        password = validated_data.pop('password', None)

        # Create the user instance using valid fields
        # Filter validated_data to include only model fields
        user = CustomUser.objects.create(**validated_data)

        # Set the password securely
        if password:
            user.set_password(password)
        user.save()
        return user
