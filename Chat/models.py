# models.py
from django.db import models
from Authentification.models import CustomUser
from django.utils import timezone


class PrivateChatRoom(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="chat_user1")
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="chat_user2")

    def get_room_name(self):
        return f"private_chat_{min(self.user1.id, self.user2.id)}_{max(self.user1.id, self.user2.id)}"


class ChatMessage(models.Model):
    room = models.ForeignKey(PrivateChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
