"""
URL configuration for codeleap_backend_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from posts import views

router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:pk>/likes/", views.LikeView.as_view(), name="post-likes"),
    path("posts/<int:pk>/comments/", views.CommentView.as_view(), name="post-comments"),
    path("posts/<int:pk>/comments/<int:comment_id>/", views.CommentRetrieveUpdateDeleteView.as_view(), name="post-comments-get-delete"),
    path('admin/', admin.site.urls),
]
