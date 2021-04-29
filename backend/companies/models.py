from django.db import models
from ..users.models import User
from ..posts.models import Post


# ====== ORGANIZATION/COMPANY CLASSES =========
class Admin(models.Model):
    user = models.ManyToManyField(User, related_name="admin")
    post = models.ManyToManyField(Post, related_name='admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# EVENT CLASSES
class Event(models.Model):
    TYPES = [
        ('GAME', "Game"),
        ('PRACTICE', "Practice"),
        ('MEETING', "Meeting"),
        ('TRAINING', "Training"),
        ('PARTY', "Party"),
        ('RECOVERY', "Recovery"),
        ('OTHER', "Other")
    ]
    event_type = models.CharField(max_length=20, choices=TYPES, default='Practice')
    admin = models.ManyToManyField(Admin, related_name="event")
    name = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/event_profile_pictures/", null=True)
    rsvp = models.ManyToManyField(User, related_name="event")
    # invited= UsersAthletesOrganizationTeamCompany
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# FACILITY ORGANIZATION TEAM COMPANY CLASSES
class Organization(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sports = []
    admin = models.ManyToManyField(Admin, related_name="organization")
    image = models.ImageField(upload_to="images/organization_profile_pictures/", null=True)
    events = models.ManyToManyField(Event, related_name="organization")
    # posts=models.ManyToManyField(Post, related_name="organization")
    # saved_posts=models.ManyToManyField(Post, related_name="organization")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Team(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name="team", on_delete=models.CASCADE)
    age_level = models.IntegerField() #Will want this to be selectable categoies per sport
    organization = models.ForeignKey(Organization, related_name="team", on_delete=models.CASCADE)
    event = models.ManyToManyField(Event, related_name="team")
    image = models.ImageField(upload_to="images/team_profile_pictures/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Coach(models.Model):
    user = models.ManyToManyField(User, related_name="coach")
    team = models.ManyToManyField(Team, related_name="coach")
    # posts=models.ManyToManyField(Post, related_name="coach")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Manager(models.Model):
    user = models.ManyToManyField(User, related_name="manager")
    team = models.ManyToManyField(Team, related_name="manager")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Trainer(models.Model):
    user = models.ManyToManyField(User, related_name="trainer")
    team = models.ManyToManyField(Team, related_name="trainer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrganizationEmployee(models.Model):
    user = models.ManyToManyField(User, related_name="organization_employee")
    organization = models.ManyToManyField(Organization, related_name="organization_employee")
    # post=models.ManyToManyField(Post, related_name="organization_employee")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/facility_profile_pictures/", null=True)
    admin = models.ManyToManyField(Admin, related_name="facility")
    sports = models.ManyToManyField(Sport, related_name="facility")
    organization = models.ManyToManyField(Organization, related_name="facility")
    event = models.ManyToManyField(Event, related_name="facility")
    created_at = models.DateTimeField(auto_now_add=True)
    # posts=models.ManyToManyField(Post, related_name="facility")
    updated_at = models.DateTimeField(auto_now=True)


class FacilityEmployee(models.Model):
    user = models.ManyToManyField(User, related_name="facility_employee")
    facility = models.ManyToManyField(Facility, related_name="facility_employee")
    # post=models.ManyToManyField(Post, related_name='facility_employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Gym(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/gym_profile_pictures/", null=True)
    sport = Sport.sport
    facility = models.ForeignKey(Facility, related_name="gym", on_delete=models.CASCADE)
    event = models.ManyToManyField(Event, related_name="gym")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Locker_Room(models.Model):
    name = models.CharField(max_length=100)
    gym = models.ManyToManyField(Gym, related_name="locker_room")
    last_cleaned = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/gym_profile_pictures/", null=True)
    sport = Sport.sport
    event = models.ManyToManyField(Event, related_name="tournament")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
