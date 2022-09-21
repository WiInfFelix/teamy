from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class RegisterSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        read_only_fields = ["password"]

    def create(self, data):
        user = User.objects.create(
            data["username"], data["email"], data["password"])


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials provided")
