from django.urls import path
from .views import SurveysView, SurveyView

urlpatterns = [
    path('',SurveysView.as_view()),
    path('<pk>',SurveyView.as_view()),
]
