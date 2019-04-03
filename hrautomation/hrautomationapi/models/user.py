from django.contrib.auth.models import User
from django.db import models


class UserExtension(models.Model):
    user = models.OneToOneField(User, related_name='role', on_delete=models.CASCADE)
    is_engineer = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    photo = models.CharField(default='', max_length=20)
