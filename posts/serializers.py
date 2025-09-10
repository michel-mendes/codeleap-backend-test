from rest_framework import serializers
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

    def update(self, instance, validated_data):
        validated_data.pop("username", None)
        return super().update(instance, validated_data)