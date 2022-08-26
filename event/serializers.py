from rest_framework import serializers
from core import models


class EventSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = models.Event
        fields = ('id', 'title', 'type')
        read_only_fields = ['id']
        depth = 1
        

class EventTypeSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = models.EventType
        fields = ('id','type')
        read_only_fields = ['id']
 