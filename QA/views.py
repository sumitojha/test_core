from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.
from django.http import HttpResponse
from rest_framework.views import  APIView
from rest_framework.authentication import (
    BasicAuthentication, TokenAuthentication)

from rest_framework.generics import ListAPIView
from serializers import QuestionSerializer, AnswerSerializer, QuestionAnswerSerializer
from .models import Question, Answer, Tenant
from profiles.models import User
from .constants import QurtionType
from .throttling import RandomRateThrottle

class QuestionAnswerView(ListAPIView):
    authentication_classes = (
        BasicAuthentication, TokenAuthentication
    )
    throttle_classes = (RandomRateThrottle,)
    serializer_class = QuestionAnswerSerializer
    queryset = Question.objects.filter(type=QurtionType.PUBLIC.value)




def index(request):
    user_count = User.objects.count()
    question_count = Question.objects.count()
    answer_count = Answer.objects.count()
    api_count = Tenant.objects.count()
    object_dic = {'user':user_count,
                  'question':question_count,
                  'answer':answer_count,
                  'tenant':api_count}
    t = loader.get_template('dashboard.html')
    c = Context({'object_list': object_dic})
    return HttpResponse(t.render(c))

