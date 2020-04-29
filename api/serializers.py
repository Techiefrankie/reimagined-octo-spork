from rest_framework import serializers
from rooms.models import Room
from meetings.models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'title', 'date', 'start_time', 'duration', 'room')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'floor', 'room_number')
