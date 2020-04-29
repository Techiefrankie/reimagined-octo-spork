from django.test import TestCase
from rooms.models import Room


# Create your tests here.
class RoomModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Room.objects.create(name='Uganda', room_number=342, floor=3)

    def test_name_content(self):
        room = Room.objects.get(pk=1)
        expected = f"{room.name}"
        self.assertEquals(expected, 'Uganda')
