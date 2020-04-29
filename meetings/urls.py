from django.urls import path
from .views import details, schedule

urlpatterns = [
    path('<int:id>', details, name='meeting_detail'),
    path('schedule/', schedule, name='schedule_meeting')
]

