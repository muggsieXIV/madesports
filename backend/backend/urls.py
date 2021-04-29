from django.urls import include, path
from django.contrib import admin


urlpatterns = (
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    # path('api-auth/companies/', include('companies.urls')),
    path('api/posts/', include('posts.urls'))
)

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
