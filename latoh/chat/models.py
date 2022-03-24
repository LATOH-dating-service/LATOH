from django.db import models
from django.contrib.auth.models import User, Group

class Chat(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE,name='group')
    user=models.ForeignKey(User, on_delete=models.CASCADE,name='user')
    text=models.TextField()