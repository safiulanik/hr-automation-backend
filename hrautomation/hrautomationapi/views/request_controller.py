from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from ..serializers.request_serializer import RequestSerializer
from ..models import Request
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class RequestListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer

    def get_queryset(self):
        user = self.request.user
        return Request.objects.filter(create_uid=user.id)


class RequestCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RequestSerializer


class RequestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class RequestListByUserAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, user_id):
        user = User.objects.get(pk=user_id)
        if user.role == 'employee':
            requests = Request.objects.filter(create_uid=user_id).order_by('-create_date')
        elif user.role == 'hr':
            requests = Request.objects.all().order_by('-create_date')
        elif user.role == 'manager':
            requests = Request.objects.filter(status='hr_reviewed').order_by('-create_date')
        else:
            requests = []
        
        return Response(
            data={
                'data': requests
            }, status=status.HTTP_200_OK, content_type='application/json'
        )
