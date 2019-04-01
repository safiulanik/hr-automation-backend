from rest_framework.urlpatterns import path
from rest_framework_jwt.views import obtain_jwt_token
from .views.request_controller import (
    RequestListAPIView,
    RequestCreateAPIView,
    RequestRetrieveUpdateDestroyAPIView
)
from .views.auth_controller import Signup, Login


urlpatterns = [
    path('request/list/', RequestListAPIView.as_view(), name='request_list'),
    path('request/', RequestCreateAPIView.as_view(), name='request_create'),
    path('request/<int:pk>', RequestRetrieveUpdateDestroyAPIView.as_view(), name='request_update'),
    path('request/list/<int:user_id>', RequestRetrieveUpdateDestroyAPIView.as_view(), name='request_update'),
    path('token-auth/', obtain_jwt_token),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view())
]
