from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .filters import PostFilter
from .paginations import CommentPagination

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    # """
    # API endpoint that allows posts to be viewed or edited.
    # """
    queryset = Post.objects.all().order_by('-created_datetime')
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = PostFilter
    filterset_fields = ["username"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_datetime", "likes"]

    


class LikeView(APIView):
    http_method_names = ["get", "post", "delete"]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk = pk)
            return Response({"likes": post.likes}, status = status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, pk):
        try:
            post = Post.objects.get(pk = pk)
            post.likes += 1
            post.save()
            
            return Response({"likes": post.likes}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk = pk)

            if (post.likes == 0):
                return Response({"likes": post.likes}, status=status.HTTP_200_OK)

            post.likes -= 1
            post.save()
            
            return Response({"likes": post.likes}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by("-created_datetime")
    http_method_names = ["get", "post", "delete"]
    pagination_class = CommentPagination
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        postId = self.kwargs["pk"]
        return Comment.objects.filter(post = postId).order_by("-created_datetime")
    
    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        comment = Comment.objects.create(
            post = post,
            username = request.data["username"],
            content = request.data["content"]
            )
        
        return Response({
            "id": comment.id,
            "username": comment.username,
            "content": comment.content
        }, status = status.HTTP_201_CREATED)
    


class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    http_method_names = ["get", "delete"]
    serializer_class = CommentSerializer

    def get(self, request, pk, comment_id = None):
        try:
            comment = Comment.objects.get(pk = comment_id, post = pk)
            return Response({
                "id": comment.id,
                "username": comment.username,
                "content": comment.content
            }, status = status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk, comment_id=None):
        try:
            comment = Comment.objects.get(pk=comment_id, post=pk)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        comment.delete()
        return Response({"message": "Comment removed"}, status=status.HTTP_204_NO_CONTENT)