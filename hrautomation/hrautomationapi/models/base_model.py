from django.db import models


class BaseModel(models.Model):
    create_uid = models.IntegerField(blank=True, null=True)
    write_uid = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
