import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from channels.db import database_sync_to_async
from channels.auth import login
from urllib.parse import parse_qs
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from chat.serializers import UserMSerializer, GroupMSerializer
from chat.models import Chat

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #Authenticate user
        self.authToken = parse_qs(self.scope['query_string'].decode())['auth'][0]
        self.user = await self.get_token_user(self.authToken)
        await login(self.scope,self.user)
        await database_sync_to_async(self.scope['session'].save)()

        self.user_groups = await self.get_json_user_groups(self.user)
        #Join groups
        for user_group in self.user_groups:
            await self.channel_layer.group_add(
                user_group['name'],
                self.channel_name
            )

        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        group_name = text_data_json['group']
        u = await self.get_json_user(self.scope['user'])
        
        await self.channel_layer.group_send(
            group_name,
            {
                'type': 'chat_message',
                'message': message,
                'group': group_name,
                'user': u
            }
        )
    
    async def chat_message(self, event):
        await self.save_message(event['group'],event['user']['id'],event['message'])
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'user': event['user']
        }))
    
    @database_sync_to_async
    def save_message(self,group_name,user_id,message):
        g = Group.objects.get(name=group_name)
        u = User.objects.get(pk=user_id)
        instance = Chat(group=g,user=u,text=message)
        instance.save()

    @database_sync_to_async
    def get_json_user_groups(self,user):
        groupInstances = user.groups.all()
        groups_json = list()
        for groupInstance in groupInstances:
            serializer = GroupMSerializer(groupInstance)
            groups_json.append(serializer.data)
        return groups_json
    
    @database_sync_to_async
    def get_json_user(self,user):
        serializer = UserMSerializer(user)
        return serializer.data
    
    @database_sync_to_async
    def get_token_user(self,token):
        tokenInstance = Token.objects.get(key=token)
        return tokenInstance.user