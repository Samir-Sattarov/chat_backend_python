from django.db import models

from users.models import UserModel


# Create your models here.
class ChatModel(models.Model):
    image = models.ImageField(default="", upload_to="uploads/")
    users = models.ManyToManyField(UserModel, default=list)
    last_message = models.CharField(default="", max_length=255)

