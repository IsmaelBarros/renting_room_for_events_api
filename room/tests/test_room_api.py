"""
Test for Room APIs.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Room

from room.serializers import RoomSerializer

ROOMS_URL = reverse('room:room-list')

def create_room(**params):
    """Create and return a sample room."""
    defaults = {
        'event' : None,
        'title': 'Sample title',
        'capacity': 20
    }
    defaults.update(**params)

    room = Room.objects.create(**defaults)
    return room

class PublicRoomAPITests(TestCase):
    """Test unauthenticated API requests"""

    def setUp(self):
        self.client = APIClient()
    
    def test_auth_required(self):
        """Test auth is required to call API."""
        
        res = self.client.get(ROOMS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateRoomAPITests(TestCase):
    """Test unauthenticated API requests"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_rooms(self):
        """Test retrieving a list of rooms."""
        
        create_room()
        create_room()

        res = self.client.get(ROOMS_URL)

        rooms = Room.objects.all().order_by('-id')
        serializer = RoomSerializer(rooms, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
