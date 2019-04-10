from rest_framework import serializers
from ..models import Request
from django.contrib.auth.models import User


class RequestListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    processed_by = serializers.SerializerMethodField()
    create_date = serializers.DateTimeField(format="%d.%M.%Y %H:%m")

    @staticmethod
    def get_created_by(obj):
        try:
            user_obj = User.objects.get(id=obj.create_uid)
            created_by = '{} {}'.format(user_obj.first_name, user_obj.last_name)
        except:
            created_by = ''
        return created_by

    @staticmethod
    def get_processed_by(obj):
        try:
            user_obj = User.objects.get(id=obj.write_uid)
            processed_by = '{} {}'.format(user_obj.first_name, user_obj.last_name)
        except:
            processed_by = ''
        return processed_by

    class Meta:
        model = Request
        fields = ('id', 'details', 'status', 'create_uid', 'write_uid',
                  'create_date', 'write_date', 'processed_by', 'created_by')


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'
