from django.db import models
from django.contrib.auth.models import User, Group
import uuid

class Chat(models.Model):
    group=models.ForeignKey(Group, related_name='chats', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"{self.user.username}: {self.text}"

class Conversation(models.Model):
    code = models.CharField(max_length=255, unique=True, default=str(uuid.uuid4()).replace("-",""), editable=False)
    name=models.CharField(max_length=255,unique=True)
    public=models.BooleanField(default=False)
    online=models.ManyToManyField(User,related_name="conversations")

    def join(self,user):
        self.online.add(user)
        self.save()
    
    def leave(self,user):
        self.online.remove(user)
        self.save()
    
    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    conversation=models.ForeignKey(Conversation,related_name="messages",on_delete=models.CASCADE)
    from_user=models.ForeignKey(User,related_name="sent_messages",on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,blank=True,related_name="received_messages",on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    read=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.conversation.name}: {self.from_user} - {self.timestamp}"