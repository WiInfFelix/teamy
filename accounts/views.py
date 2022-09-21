from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken

from accounts.serializers import LoginSerializer, RegisterSerialzer, UserSerializer
# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = RegisterSerialzer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = AuthToken.objects.create(user)

        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context).data,
            "token": token[1]
        })


class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def
