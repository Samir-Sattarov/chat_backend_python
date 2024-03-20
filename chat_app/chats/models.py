from django.db import models

from users.models import UserModel


# Create your models here.


class ChatModel(models.Model):
    image = models.ImageField(default="", upload_to="uploads/")
    users = models.ManyToManyField(UserModel, default=list)
    last_message = models.CharField(default="", max_length=255)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)


class MessageModel(models.Model):
    message = models.CharField(default="", max_length=255)
    roomId = models.ForeignKey(ChatModel, on_delete=models.CASCADE, related_name='roomId')
    userId = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
