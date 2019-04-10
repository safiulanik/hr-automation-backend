from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from ..serializers.request_serializer import *
from ..models import Request
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class RequestListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role and user.role.is_hr:
            return Request.objects.all()
        elif user.role and user.role.is_manager:
            return Request.objects.filter(status='hr_reviewed')
        elif user.role and user.role.is_engineer:
            return Request.objects.filter(create_uid=user.id)
        else:
            return []


class RequestCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer


class RequestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
