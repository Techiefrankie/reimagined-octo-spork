from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200, null=False)
    floor = models.IntegerField(null=False)
    room_number = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.name}: Room {self.room_number} on {self.floor} floor"
