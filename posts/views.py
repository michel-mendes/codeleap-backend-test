from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows posts to be viewed or edited.
    # """
    queryset = Post.objects.all().order_by('-created_datetime')
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = PostSerializer