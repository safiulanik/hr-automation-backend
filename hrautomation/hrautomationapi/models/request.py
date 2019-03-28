from django.db import models
from .base_model import BaseModel


class Request(BaseModel):
    details = models.TextField()
    status = models.CharField(max_length=20, null=False, default='open')
