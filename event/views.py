from core.models import Event, EventType
from event import serializers 

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class EventViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EventSerializer
        
        return self.serializer_class  
    
    def create(self, request, *args, **kwargs):
        
        user = request.user

        if user.is_staff:
            data = request.data
            print(data)
            new_event = Event.objects.create(
                title=data['title'],
                type= EventType.objects.get(pk=data['type']))
            
            new_event.save()
            serializer = serializers.EventSerializer(new_event)
            return Response(serializer.data)
        
        return Response(
            {'error': 'Only staff members are allowed to create events'},
            status=status.HTTP_401_UNAUTHORIZED)


class EventTypeViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.EventTypeSerializer
    queryset = EventType.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        
        user = request.user

        if user.is_staff:
            data = request.data
            new_event_type = EventType.objects.create(
                type=data['type']
            )
            new_event_type.save()

            serializer = serializers.EventTypeSerializer(new_event_type)            
            return Response(serializer.data)
        
        return Response(
            {'error': 'Only staff members are allowed to create event types'},
            status=status.HTTP_401_UNAUTHORIZED)
        




