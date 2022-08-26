from rest_framework import serializers
from core import models
from user.serializers import UserSerializer
from room.serializers import RoomSerializer

class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    room = RoomSerializer()
    class Meta:
        model = models.Book
        fields = ('id', 'user', 'room')
        read_only_fields = ['id']
        depth = 1
        

