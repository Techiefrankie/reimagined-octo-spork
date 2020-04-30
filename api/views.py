from django.shortcuts import get_object_or_404
from rest_framework import generics
from rooms.models import Room
from meetings.models import Meeting
import api.serializers as serializer


# Create your views here.
class MeetingAPIView(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = serializer.MeetingSerializer


class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = serializer.RoomSerializer


class RetrieveRoomAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = serializer.RoomSerializer


class RetrieveMeetingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = serializer.MeetingSerializer
