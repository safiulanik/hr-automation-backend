from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from ..serializers.request_serializer import RequestSerializer
from ..models import Request


class RequestListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer
    queryset = Request.objects.all()


class RequestCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer


class RequestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
