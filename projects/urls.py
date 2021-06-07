from django.urls import path
from .views import ProjectsView, ProjectView, SearchView

urlpatterns = [
    path('',ProjectsView.as_view()),
    path('search',SearchView.as_view()),
    path('<pk>',ProjectView.as_view())
]
