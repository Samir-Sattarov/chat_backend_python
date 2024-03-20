from rest_framework import  generics

from chats.serializers import ChatSerializer
from chats.models import ChatModel


# Create your views here.
class ChatListView(generics.ListAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ChatSerializer


