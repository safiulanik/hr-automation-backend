from rest_framework.urlpatterns import path
from .views.request_controller import (
    RequestListAPIView,
    RequestCreateAPIView,
    RequestRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('request/list/', RequestListAPIView.as_view(), name='request_list'),
    path('request/', RequestCreateAPIView.as_view(), name='request_create'),
    path('request/<int:pk>', RequestRetrieveUpdateDestroyAPIView.as_view(), name='request_update'),
]
