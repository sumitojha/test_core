from rest_framework import serializers
from .models import Question, Answer , Tenant
from profiles.serializers import UserSerializer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Answer
        fields = ('id','user', 'body')


class QuestionAnswerSerializer(serializers.ModelSerializer):
        answer = serializers.SerializerMethodField()
        user = UserSerializer()
        class Meta:
            model = Question
            fields = ('id','user', 'title','answer',)

        def get_answer(self, obj):
            answer = Answer.objects.filter(question_id=obj.id)
            return AnswerSerializer(answer, many=True).data