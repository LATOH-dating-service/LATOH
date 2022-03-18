from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ChannelGroup
from .serializers import ChannelGroupSerializer

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

class ChannelGroupViewSet(viewsets.ModelViewSet):
    queryset=ChannelGroup.objects.all()
    serializer_class=ChannelGroupSerializer
    permission_classes=[permissions.IsAuthenticated]