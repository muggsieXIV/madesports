from django.contrib import admin
from .models import User, Athlete, Family


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone', 'image', 'password')


class AthleteAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'password', 'date_of_birth')


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'password', 'created_at', 'updated_at')



admin.site.register(User)

admin.site.register(Athlete)

admin.site.register(Family)
