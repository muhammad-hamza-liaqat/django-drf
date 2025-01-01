from rest_framework import serializers
from custom_auth.models import User
from django.contrib.auth.hashers import check_password

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("User with this email does not exist.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid password.")

        data['user'] = user
        return data
