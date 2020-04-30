from rest_framework import viewsets, permissions, generics
from rooms.models import Room
from meetings.models import Meeting
from django.contrib.auth import get_user_model
import api.serializers as serializer
from api.permissions import IsCreatorOrReadOnly


# Create your views here.

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = serializer.RoomSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsCreatorOrReadOnly, permissions.IsAuthenticated)
    queryset = Meeting.objects.all()
    serializer_class = serializer.MeetingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializer.UserSerializer


class GenericListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = serializer.RoomSerializer


class GenericUnsafeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = serializer.RoomSerializer
