from django.db import models
from datetime import time
from rooms.models import Room
from django.contrib.auth.models import User


# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=30)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.title} starts at {self.start_time} on {self.date} for a duration of {self.duration} minutes"
