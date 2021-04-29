from .models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer

# Post ViewSet
# Viewsets allow a full CRUD API [Read Write Update Delete]
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer
