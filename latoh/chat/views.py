from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group

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