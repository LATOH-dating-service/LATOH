from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, ChatSerializer
from django.contrib.auth.models import User, Group
from chat.models import Chat

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
    
class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]

class ChatViewset(viewsets.ModelViewSet):
    queryset=Chat.objects.all()
    serializer_class=ChatSerializer
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=['GET'],detail=False)
    def get_group_messages(self,request):
        group = Group.objects.get(pk=request.query_params['group_id'][0])
        messages = Chat.objects.filter(group=group)
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)