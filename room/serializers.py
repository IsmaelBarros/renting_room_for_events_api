from typing import Optional
from rest_framework import serializers
from core import models


class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Room
        fields = ('id', 'event', 'title','capacity')
        optional_fields = ['event', ]
        read_only_fields = ['id']
        depth = 2
        

