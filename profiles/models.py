from __future__ import unicode_literals
import uuid
from django.conf import settings
from django.db import models

# Create your models here.


class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'




