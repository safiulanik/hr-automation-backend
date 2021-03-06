from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
import re
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from hrautomation.local_settings import EMAIL_DOMAIN, EMAIL_DOMAIN_EXTENSION


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'id')


def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@(?:(?:[a-zA-Z0-9-]+\.)?[a-zA-Z]+\.)?({})\.{}".format(EMAIL_DOMAIN, EMAIL_DOMAIN_EXTENSION)
    if not re.match(pattern, email):
        raise serializers.ValidationError('Required email format: <username>@misfit.tech')
    return email


def validate_role(role):
    if role not in ['engineer', 'hr', 'manager']:
        raise serializers.ValidationError('Invalid role')
    return role


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    email = serializers.CharField(required=True, validators=[
        validate_email,
        UniqueValidator(queryset=User.objects.all())
    ])

    username = serializers.CharField(required=True, validators=[
        UniqueValidator(queryset=User.objects.all())
    ])

    # role = serializers.CharField(required=True, validators=validate_role)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'email', 'password', 'first_name', 'last_name', 'username', 'id')
