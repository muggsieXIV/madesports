from django.db import models
import re


# Create your models here.
# ***** USER VALIDATING ******
class UserManager(models.Manager):
    def user_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form_data['first_name']) < 2:
            errors['first_name'] = "First Name is not long enough. Try again!"
        if len(form_data['last_name']) < 2:
            errors['last_name'] = "Last Name is not long enough. Try again!"
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right, try again!"
        if len(form_data['password']) < 8:
            errors['password'] = "Password is not long enough, try again!"
        if form_data['password'] != form_data['confirm_password']:
            errors['confirm_password'] = "Passwords don't match! Try again!"
        return errors

    def login_validator(self, form_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form_data['email']):
            errors['email_format'] = "Email Doesn't look right!"
        if form_data['email'] != User.email:
            errors['email_not_found'] = "Email not found, try again!"
        return errors

# ==== USER CLASS ====
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(null=True)
    image = models.ImageField(upload_to='static/images/user_profile_pictures/', null=True)
    password = models.CharField(max_length=100)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # USER is a PARENT of [ Family -> Athlete, Organization -> Team, Company ]

    class Meta:
        ordering = ('first_name', 'last_name', 'email', 'phone', 'image', 'password')

    def __str__(self):
        return self.username


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
        if form_data['confirm_password'] != form_data['password']:
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
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ===== TO DO =========
    # Add image field
    # Make a foriegn key for athlete to family... May need to dropDB to do this... maybe wait until
    # postresql migration

    # Athlete is connected by a team. An Athlete cannot connect
    # themself to a team/camp/org, admins must request to add them.

    class Meta:
        ordering = ("created_at",  "updated_at", "first_name", "last_name", "username", "password", "date_of_birth")

    def __str__(self):
        return self.username


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
        return self.username


# # ==== RELATIVE CLASS ====
# class Relative(models.Model):
#     user = models.ForeignKey(User, related_name="relative")
#     relation = models.CharField(max_length=100)
#     family = models.ManyToManyField(Family, related_name="relative")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     # Relatives have (( READ_ONLY )) access to family accounts.
#     # Relatives permissions set_by(PARENTS.settings)
#
#     def __str__(self) -> User:
#         return self.user
