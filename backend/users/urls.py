# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
#
#
# urlpatterns = [
#     path('users', views.user_list),
#     path('user/<int:pk>', views.user_detail),
#
#     path('athletes', views.athlete_list),
#     path('athlete/<int:pk>', views.athlete_detail),
#
#     path('families', views.family_list),
#     path('family/<int:pk>', views.family_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from rest_framework import routers
from .api import UserViewSet, AthleteViewSet, FamilyViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('athletes', AthleteViewSet, 'athletes')
router.register('families', FamilyViewSet, 'families')

urlpatterns = router.urls

