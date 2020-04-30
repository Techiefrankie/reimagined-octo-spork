from django.urls import path
import api.views as api_views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', api_views.UserViewSet, basename='users')
# router.register('rooms', api_views.RoomViewSet, basename='rooms')
router.register('meetings', api_views.MeetingViewSet, basename='meetings')

urlpatterns = router.urls
urlpatterns.append(path('rooms/', api_views.RoomListView.as_view()),)
urlpatterns.append(path('rooms/<int:pk>', api_views.RoomRUDView.as_view()),)

# urlpatterns = [
#     path('meetings/list', api_views.MeetingAPIView.as_view()),
#     path('rooms/list', api_views.RoomViewSet.as_view()),
#     path('rooms/<int:pk>/', api_views.RetrieveRoomAPIView.as_view()),
#     path('meetings/<int:pk>/', api_views.MeetingViewSet.as_view())
# ]
