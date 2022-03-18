from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChannelGroup(models.Model):
    identity = models.UUIDField(unique=True,auto_created=True)

class UserChannelGroup(models.Model):
    group=models.ForeignKey(ChannelGroup, on_delete=models.CASCADE,name='group')
    user=models.ForeignKey(User, on_delete=models.CASCADE,name='user_channel_group.user')

class Chat(models.Model):
    group=models.ForeignKey(ChannelGroup, on_delete=models.CASCADE,name='group')
    user=models.ForeignKey(User, on_delete=models.CASCADE,name='chat.user')
    message=models.TextField()