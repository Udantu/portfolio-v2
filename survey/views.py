from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Survey, Question, Answer
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer
from datetime import datetime, timezone, timedelta

class SurveysView(ListAPIView):
    queryset = Survey.objects.order_by('pk')
    permission_classes = (permissions.AllowAny, )
    serializer_class = SurveySerializer

class SurveyView(ListAPIView):
    queryset = Question.objects.order_by('pk')
    permission_classes = (permissions.AllowAny, )
    serializer_class = QuestionSerializer
    print("test")

    def post(self,request,pk,format=None):
        questions = Question.objects.order_by('pk').filter(survey='pk')
        data = self.request.data
        if len(questions) != len(data):
            return Response({'error':'please fill out all of the questions'})
        else:
            print('keep going')
