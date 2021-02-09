from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


# Create your models here.
# ***** USER VALIDATING ******
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Superusers must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        return user

# ==== USER CLASS ====
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='static/images/user_profile_pictures/', null=True)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)
    objects = UserManager()
    # saved_posts=models.ManyToManyField(Post, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return self.email


# **** ATHLETE VALIDATING ****
class AthleteManager(models.Manager):

    def athlete_validator(self, form_data):
        errors = {}
        if len(form_data['first_name']) < 2:
            errors['first_name'] = "First Name is not long enough. Try again!"
        if len(form_data['last_name']) < 2:
            errors['last_name'] = "Last Name is not long enough. Try again!"
        if len(form_data['username']) < 8:
            errors['username'] = "Username must be at least 8 characters. Try again!"
        if len(form_data['password']) < 8:
            errors['password'] = "Password is not long enough, try again!"
        if form_data['password'] != form_data['confirm_password']:
            errors['confirm_password'] = "Passwords don't match! Try again!"
        return errors 

    def login_validator(self, form_data):
        errors = {}
        if len(form_data['username']) != Athlete.username:
            errors['username'] = "Username not recognized, try again."
        if len(form_data['password']) != Athlete.password:
            errors['password'] = "Password does not match the one associated to your username, try again!"
        return errors 


# ==== ATHLETE CLASS ====
class Athlete(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # teams=models.ManyToManyField(Team, related_name="athlete")
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("created_at",  "updated_at", "first_name", "last_name", "username", "password", "date_of_birth")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.username}, {self.password}, {self.created_at}, {self.updated_at}, {self.date_of_birth}"


# **** FAMILY VALIDATING ****
class FamilyManager(models.Model):

    def family_validator(self, form_data):
        errors = {}
        if len(form_data['name']) < 2:
            errors['name'] = "Please provide your full family name"
        if len(form_data['username']) < 8:
            errors['username'] = "User name must be a at least 8 characters."
        if len(form_data['pin']) < 8:
            errors['password'] = "Your password must be at least 8 characters long."
        return errors

    def login_validator(self, form_data):
        errors = {}
        if form_data['username'] != Family.username:
            errors['username'] = "Username doesn't match one on file, please check spelling"
        if form_data['password'] != Family.password:
            errors['password'] = "Password is not correct, try again"

# ==== FAMILY CLASS ====
class Family(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    parents = models.ManyToManyField(User, related_name="family")
    athletes = models.ManyToManyField(Athlete, related_name="family")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name", "username", "password")

    def __str__(self):
        return f"{self.name}, {self.username}, {self.password}"


# ==== RELATIVE CLASS ====
# class Relative(models.Model):
#     user=models.ManyToManyField(User, related_name="relative")
#     relation=models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
