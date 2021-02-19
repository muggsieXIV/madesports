from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'sub_categories', 'title', 'description', 'user', 'image', 'post_type')


admin.site.register(Post)
