from __future__ import unicode_literals
import uuid
from django.db import models
from profiles.models import User
import datetime
from rest_framework import serializers
# Create your models here.
from .constants import QUESTION_TYPE

class Question(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name="question_user")
    title = models.CharField(max_length=150)
    type = models.PositiveIntegerField(choices=QUESTION_TYPE)

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    body = models.TextField()
    user = models.ForeignKey(User, related_name="answer_user")
    question = models.ForeignKey(Question, related_name="answer_question")

    class Meta:
        db_table = 'answer'


class Tenant(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    api_key = models.URLField(max_length=500)
    count = models.PositiveIntegerField(default=0)
    last_modified = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'tenant'

