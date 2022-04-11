from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import MeetSerializer
from .models import Meet

# Create your views here.
class MeetViewset(viewsets.ModelViewSet):
    queryset=Meet.objects.all()
    serializer_class=MeetSerializer
    permission_classes=[permissions.IsAuthenticated]