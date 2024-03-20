from django.shortcuts import render
from rest_framework import generics

from users.models import UserModel
from users.serializers import UserSerializer


# Create your views here.
class UserListView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
