from django.shortcuts import render
from rest_framework import generics

from users.models import UserModel
from users.serializers import UserSerializer

from rest_framework.permissions import *


# Create your views here.
class UserListView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
