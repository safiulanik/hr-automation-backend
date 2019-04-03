from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.auth_serializer import UserSerializer, UserSerializerWithToken
from ..models.user import UserExtension


class Login(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class Signup(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        role = request.data.get('role')
        if serializer.is_valid():
            serializer.save()
            new_user_id = serializer.data.get('id')
            UserExtension.objects.create(**{
                'user_id': new_user_id,
                'is_engineer': True if role == 'engineer' else False,
                'is_hr': True if role == 'hr' else False,
                'is_manager': True if role == 'manager' else False
            })
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
