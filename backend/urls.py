from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from backend.posts.views import PostViewSet
from backend.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)


# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
