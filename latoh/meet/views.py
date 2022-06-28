from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MeetSerializer
from .models import Meet

# Create your views here.
class MeetViewset(viewsets.ModelViewSet):
    queryset=Meet.objects.all()
    serializer_class=MeetSerializer
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=['GET'],detail=False)
    def get_full_meets(self,request):
        meets = Meet.objects.all()
        meetsDict = MeetSerializer(meets, many=True)

        a = list()

        for meetDict in meetsDict.data:
            b = meetDict
            for key, value in meetDict.items():
                if key == 'user':
                    c = User.objects.get(pk=value)
                    b[key]={'id':c.id,'username':c.username}
            a.append(b)

        return Response(a)