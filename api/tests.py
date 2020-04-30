from django.test import TestCase
from rooms.models import Room
from meetings.models import Meeting
from django.contrib.auth.models import User


# Create your tests here.
class RoomModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Room.objects.create(name='Uganda', room_number=342, floor=3)

    def test_name_content(self):
        room = Room.objects.get(pk=1)
        expected = f"{room.name}"
        self.assertEquals(expected, 'Uganda')


class MeetingTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a new user
        user = User(username='techie', email='techie@gmail.com', password='Password12')
        user.save()

        # create room
        room = Room(name='Uganda', room_number=342, floor=3)
        room.save()

        # create a new meeting schedule
        meeting = Meeting(title='test meeting', date='2020-04-29', start_time='09:00:00', duration=30, created_by=user
                          , room=room)
        meeting.save()

    # test conditions
    def test_content(self):
        meeting = Meeting.objects.get(id=1)
        created_by = meeting.created_by.username
        title = meeting.title
        room = meeting.room.name
        self.assertEquals(created_by, 'techie')
        self.assertEquals(title, 'test meeting')
        self.assertEquals(room, 'Uganda')
