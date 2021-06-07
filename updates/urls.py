from django.urls import path
from .views import UpdatesView

urlpatterns = [
    path('',UpdatesView.as_view()),
]
