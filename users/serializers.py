from rest_framework import serializers
from .models import User, Athlete, Family



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'image', 'password')


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ('first_name', 'last_name', 'username', 'password', 'date_of_birth')


class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Family
        fields = ('name', 'username', 'password', 'parents', 'athletes')
