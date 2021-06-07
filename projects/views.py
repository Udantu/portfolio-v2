from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Project
from django.db.models import Q
from .serializers import ProjectSerializer, ProjectDetailSerializer

class ProjectsView(ListAPIView):
    queryset = Project.objects.order_by('-pk')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

class ProjectView(RetrieveAPIView):
    queryset = Project.objects.order_by('-pk')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectDetailSerializer
    lookup_field = 'pk'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProjectSerializer

    def get(self,request,format=None):
        queryset = request.data['keywords']
        queries = queryset.split(" ")
        p = []
        for q in queries:
            programs = (Project.objects.order_by('-pk')).filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(tag__icontains=q)
            ).distinct()


            for program in programs:
                p.append(program)

        serializer = ProjectSerializer(p,many=True)

        return Response(serializer.data)
