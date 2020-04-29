"""
urls for managing room's app
"""

from django.urls import path
from .views import list, detail

urlpatterns = [
    path('list/', list, name='room_list'),
    path('<int:id>', detail, name='room_detail')
]
