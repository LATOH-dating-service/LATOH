from rest_framework import serializers
from .models import *

class ChannelGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ChannelGroup
        fields=['identity']