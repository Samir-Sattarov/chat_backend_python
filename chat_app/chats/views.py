from django.utils import timezone

from rest_framework import generics
from rest_framework.response import Response

from chats.serializers import *
from chats.models import *


# Create your views here.
class ChatListView(generics.ListCreateAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ChatSerializer


class MessageListView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_id = self.request.query_params.get('roomId')

        current_time = timezone.now()

        queryset = MessageModel.objects.all()
        if room_id:
            queryset = queryset.filter(roomId=room_id)

        queryset = queryset.filter(created_at__gte=current_time - timezone.timedelta(days=1))

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        return Response(
            dict(data=serializer.data)
        )
