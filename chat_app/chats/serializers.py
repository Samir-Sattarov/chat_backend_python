from rest_framework import serializers

from chats.models import ChatModel
from users.serializers import UserSerializer


class ChatSerializer(serializers.ModelSerializer):
    users = UserSerializer

    class Meta:
        model = ChatModel
        fields = "__all__"
