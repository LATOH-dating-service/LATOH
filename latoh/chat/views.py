from urllib import request
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ChatMSerializer, UserMSerializer, GroupMSerializer, ConversationSerializer, MessageSerializer
from django.contrib.auth.models import User, Group
from chat.models import Chat,Conversation,Message

# Create your views here.
class ConversationListView(generic.ListView):
    model=Conversation
    context_object_name = "conversations"

    def get_queryset(self):
        return self.request.user.conversations.all()
    

class ConversationDetailView(generic.DetailView):
    model=Conversation
    context_object_name = "conversation"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conversation"] = ConversationSerializer(self.object).data
        return context
    
    def get_queryset(self):
        return self.request.user.conversations.all()   
    
    
class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserMSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupMSerializer
    permission_classes=[permissions.IsAuthenticated]

class ChatViewset(viewsets.ModelViewSet):
    queryset=Chat.objects.all()
    serializer_class=ChatMSerializer
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=['GET'],detail=False)
    def get_group_messages(self,request):
        group = Group.objects.get(pk=request.query_params['group_id'][0])
        messages = Chat.objects.filter(group=group)
        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)

class ConversationViewset(viewsets.ModelViewSet):
    queryset=Conversation.objects.all()
    serializer_class=ConversationSerializer

class MessageViewset(viewsets.ModelViewSet):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer