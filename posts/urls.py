from django.urls import path
from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializers import PostSerializer


urlpatterns = [
    path('post/', ListCreateAPIView.as_view(queryset=Post.objects.all(), serializer_class=PostSerializer), name='post-list')
]