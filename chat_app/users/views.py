from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import UserModel
from users.serializers import UserSerializer

from rest_framework.permissions import *


# Create your views here.
class UserListView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class GetCurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(dict(data=serializer.data))
