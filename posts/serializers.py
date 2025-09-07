from rest_framework import serializers, status
from rest_framework.response import Response
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "username", "created_datetime", "title", "content"]
        read_only_fields = ["id", "created_datetime"]
        extra_kwargs = {
            'username': { 'required': True }
        }

    def validate(self, data):
        if self.instance and "username" in data:
            raise serializers.ValidationError(
                {"username": "Can not be changed."}
            )
        return data
