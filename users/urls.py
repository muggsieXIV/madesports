from django.urls import path
from rest_framework.generics import ListCreateAPIView

from .models import User, Athlete, Family
from .serializers import UserSerializer, AthleteSerializer, FamilySerializer


urlpatterns = [
    path('users/', ListCreateAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),
    path('families/', ListCreateAPIView.as_view(queryset=Family.objects.all(), serializer_class=FamilySerializer), name='family-list'),
    path('athletes/', ListCreateAPIView.as_view(queryset=Athlete.objects.all(), serializer_class=AthleteSerializer), name='athlete-list')
]
