from django.db import models

# Create your models here.

class Conversation(models.Model):
    user_phone = models.CharField(max_length=20)
    started_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=10, choices=[('user', "User"), ('bot', "Bot")])
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)