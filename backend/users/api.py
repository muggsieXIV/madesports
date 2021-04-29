from .models import User, Athlete, Family
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, AthleteSerializer, FamilySerializer


# View sets allow a full CRUD API [Read Write Delete]

# User ViewSets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


# Athlete ViewSet
class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AthleteSerializer


# Family ViewSet
class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FamilySerializer
