from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meet(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='static/meet')
    description=models.CharField(max_length=255,null=True)