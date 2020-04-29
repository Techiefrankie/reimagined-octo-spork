from django.urls import path
import api.views as api_views

urlpatterns = [
    path('meetings/list', api_views.MeetingAPIView.as_view()),
    path('rooms/list', api_views.RoomAPIView.as_view()),
    path('rooms/<int:pk>/', api_views.RetrieveRoomAPIView.as_view()),
    path('meetings/<int:pk>/', api_views.RetrieveMeetingAPIView.as_view())
]

