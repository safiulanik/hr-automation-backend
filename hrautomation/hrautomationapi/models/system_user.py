from django.db import models
from django.contrib.auth.models import User
from .base_model import BaseModel


class SystemUser(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=20, default='', null=True)
    role = models.CharField(max_length=20, null=False, default='admin')
