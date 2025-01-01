from rest_framework import serializers
from custom_auth.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "id","email", "password"]
