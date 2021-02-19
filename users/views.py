from rest_framework import viewsets, permissions
from .serializers import UserSerializer, FamilySerializer, AthleteSerializer
from django.contrib.auth.models import User
# from django.contrib.auth.models import Athlete
# from django.contrib.auth.models import Family
from .models import Athlete, Family



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class FamilyViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows families to be viewed or edited.
    """
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]


class AthleteViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows athletes to be viewed or edited.
    """
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticated]




