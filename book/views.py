from core.models import Book, Room
from book import serializers 

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.BookSerializer
    queryset = Book.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookSerializer
        
        return self.serializer_class 
    
    def create(self, request, *args, **kwargs):

        data = request.data       

        new_book = Book.objects.create(
            user=self.request.user,
            room=Room.objects.get(pk=data['room']))
        event_type = new_book.room.event.type.type

        room = Room.objects.get(pk=data['room'])

        if room.capacity <= 0:
            return Response(
                {'error': 'Sold out.There is no more capacity for this room.'},
                status=status.HTTP_403_FORBIDDEN)    
        
        if event_type == 'public':   
            room.capacity -= 1
            new_book.save()                    
            room.save()                    
            serializer = serializers.BookSerializer(new_book)
            return Response(serializer.data)
        
        return Response(
            {'error': 'You are allowed to book public rooms only.'},
            status=status.HTTP_403_FORBIDDEN)


        
