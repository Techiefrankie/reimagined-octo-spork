from rest_framework import serializers
from rooms.models import Room
from meetings.models import Meeting
from django.contrib.auth import get_user_model


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'title', 'date', 'start_time', 'duration', 'room', 'created_by')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'floor', 'room_number')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')
