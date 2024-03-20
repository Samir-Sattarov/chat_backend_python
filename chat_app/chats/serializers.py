from rest_framework import serializers

from chats.models import ChatModel, MessageModel
from users.serializers import UserSerializer


class ChatSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = ChatModel
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    roomId = serializers.PrimaryKeyRelatedField(queryset=ChatModel.objects.all())  # Используем PrimaryKeyRelatedField для вывода только id комнаты
    userId = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MessageModel
        fields = "__all__"
