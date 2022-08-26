from core.models import Room, Event
from room import serializers 

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.RoomSerializer
    queryset = Room.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RoomSerializer
        
        return self.serializer_class      
    
    
    def create(self, request, *args, **kwargs):

        user = request.user

        if user.is_staff:
            data = request.data

            if data['event'] is None:
                new_room = Room.objects.create(
                    event=None,
                    title=data['title'],
                    capacity=data['capacity'])

            else:
                event = Event.objects.get(pk=data['event'])
                if event is not None:
                    new_room = Room.objects.create(
                        event=Event.objects.get(pk=data['event']),
                        title=data['title'],
                        capacity=data['capacity'])                
                
            new_room.save()
            serializer = serializers.RoomSerializer(new_room)
            return Response(serializer.data)

        return Response(
            {'error': 'Only staff members are allowed to create rooms'},
            status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        
        user = request.user

        if user.is_staff:
            data = request.data

            room_with_no_event = Room.objects.filter(id=data['id']).filter(event=None)

            if room_with_no_event is not None:  
                room_with_no_event.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            return Response(
                {'Warning': 'All rooms have events'},
                status=status.HTTP_404_NOT_FOUND)

        return Response(
            {'error': 'Only staff members are allowed to delete rooms'},
            status=status.HTTP_401_UNAUTHORIZED)

        
        
