from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('post_type', 'category', 'sub_categories', 'title', 'description', 'user', 'image', 'created_at')

