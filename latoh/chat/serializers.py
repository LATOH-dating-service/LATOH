from rest_framework import serializers
from django.contrib.auth.models import User, Group
from chat.models import Chat

class UserMSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=['url','name']

class ChatMSerializer(serializers.ModelSerializer):
    user = UserMSerializer(many=False,read_only=True)
    class Meta:
        model=Chat
        fields='__all__'

class GroupMSerializer(serializers.ModelSerializer):
    users = UserMSerializer(many=True,read_only=True)
    class Meta:
        model=Group
        fields='__all__'

class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Chat
        fields='__all__'