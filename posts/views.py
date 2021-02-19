from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions, viewsets


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-date_joined')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
