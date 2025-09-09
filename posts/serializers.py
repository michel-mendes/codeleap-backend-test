from rest_framework import serializers, status
from rest_framework.response import Response
from .models import Post, Comment

# Bonus --v
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "username", "content", "created_datetime"]
        read_only_fields = ["id", "post", "created_datetime"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "username",
            "created_datetime",
            "title",
            "content",
            "likes",
            "comments"
            ]
        read_only_fields = ["id", "created_datetime", "likes", "comments", ]
        extra_kwargs = {
            'username': { 'required': True }
        }

    def validate(self, data):
        data.pop("username", None)
        return data
