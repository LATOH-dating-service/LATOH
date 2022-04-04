from django.db import models
from django.contrib.auth.models import User, Group

class Chat(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE,name='group')
    user=models.ForeignKey(User, on_delete=models.CASCADE,name='user')
    text=models.TextField()
    date=models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"{self.user.username}: {self.text}"