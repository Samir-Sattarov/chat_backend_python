from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import MessageModel, ChatModel


@receiver(post_save, sender=MessageModel)
def update_last_message_in_chat(sender, instance, created, **kwargs):
    if created:
        chat = instance.roomId
        message = instance.message
        chat.last_message = message
        chat.last_message_at = timezone.now()
        chat.save()
