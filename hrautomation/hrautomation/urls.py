from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('hrautomationapi.urls')),
]
