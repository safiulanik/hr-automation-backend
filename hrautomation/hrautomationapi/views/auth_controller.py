from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.auth_serializer import UserSerializer, UserSerializerWithToken


class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class Signup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
