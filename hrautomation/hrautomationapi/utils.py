from .serializers.auth_serializer import UserSerializer
from .models.user import UserExtension


def custom_jwt_response_handler(token, user=None, request=None):
    user_data = UserSerializer(user, context={'request': request}).data
    role = UserExtension.objects.filter(user_id=int(user_data.get('id')))
    if role:
        user_data['photo'] = role[0].photo
        if role[0].is_engineer:
            user_data['role'] = 'engineer'
        elif role[0].is_hr:
            user_data['role'] = 'hr'
        elif role[0].is_manager:
            user_data['role'] = 'manager'
    return {
        'token': token,
        'user': user_data
    }
