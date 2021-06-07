from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer

class UpdatesView(ListAPIView):
    queryset = Post.objects.order_by('-date_posted')
    permission_classes = (permissions.AllowAny, )
    serializer_class = PostSerializer
