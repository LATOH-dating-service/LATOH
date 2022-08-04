from django.db import models
from django.contrib.auth.models import User, Group

class Chat(models.Model):
    group=models.ForeignKey(Group, related_name='chats', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"{self.user.username}: {self.text}"