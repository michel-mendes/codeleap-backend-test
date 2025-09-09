from django.db import models

# Create your models here.

class Post(models.Model):
    # id = models.PositiveBigIntegerField(primary_key = True)
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    # id = models.PositiveBigIntegerField(primary_key = True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)