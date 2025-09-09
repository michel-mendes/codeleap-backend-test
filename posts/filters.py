import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="username", lookup_expr="icontains")

    class Meta:
        model = Post
        fields = ["username"]