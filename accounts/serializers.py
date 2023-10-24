from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CustomUser
        fields = ['id', 'username', 'email']


class CustomUserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        extra_kwargs ={'password1': {'write_only': True}, 'password2': {'write_only': True}}


class CustomUserLoginSerializer(LoginSerializer):
    email = None
    username = serializers.CharField(required=True)



