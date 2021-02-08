from django.contrib.auth.models import User
from django.db import models
# Create your models here.
# from .backends.users.models import User


class Category(models.Model):
    CATEGORY = [
        ('MED', 'Medical'),
        ('FIT', 'Fitness'),
        ('FUT', 'Futball'),
        ('HKY', 'Hockey'),
        ('BSK', 'Basketball'),
    ]
    category=models.CharField(max_length=20, choices=CATEGORY, default='Medical')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PostType(models.Model):
    TYPES = [
        ('BLG', 'Blog'),
        ('DRL', 'Drill'),
        ('PRP', 'Practice Plan'),
    ]
    post_type=models.CharField(max_length=100, choices=TYPES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SubCategory(models.Model):
    category=models.ManyToManyField(Category, related_name="sub_categories")
    MED_SUB_CAT = [
        ('NUT', 'Nutrition'),
        ('CNC', 'Concussion'),
        ('IRH', 'Injury Rehabilitation'),
        ('SRB', 'Surgical Rehabilitation'),
        ('IPV', 'Injury Prevention'),
        ('MTH', 'Mental Health'),
    ]
    FIT_SUB_CAT = [
        ('RVY', 'Recovery'),
        ('FLX', 'Flexibility'),
        ('MBT', 'Mobility'),
        ('VIS', 'Vision'),
        ('STG', 'Strength'),
        ('CON', 'Conditioning'),
        ('SPD', 'Speed'),
    ]
    FUT_SUB_CAT = [
        ('DRB', 'Dribbling'),
        ('SYS', 'Systems'),
        ('CON', 'Conditioning'),
        ('SHT', 'Shooting'),
        ('PSS', 'Passing'),
        ('AGL', 'Agility'),
        ('ATK', 'Attacking'),
        ('DEF', 'Defending'),
        ('GMP', 'Game Play'),
    ]
    HKY_SUB_CAT = [
        ('SYS', 'Systems'),
        ('PPL', 'Power Play'),
        ('PNK', 'Penalty Kill'),
        ('FCO', 'Face Offs'),
        ('CON', 'Conditioning'),
        ('SHT', 'Shooting'),
        ('PSS', 'Passing'),
        ('STK', 'Stickhandling'),
        ('EDG', 'Edges'),
        ('OVR', 'Overspeed'),
        ('BTL', 'Battle'),
        ('SMA', 'Small Area'),
        ('FLI', 'Full Ice'),
        ('OFI', 'Off Ice'),
    ]
    BSK_SUB_CAT = [
        ('DBL', 'Dribbling'),
        ('SHT', 'Shooting'),
        ('PSS', 'Passing'),
        ('DEF', 'Defensive'),
        ('OFF', 'Offensive'),
        ('MOV', 'Movement'),
    ]

    category_set=Category.category
    if category_set == 'Medical':
        sub_categories = models.CharField(max_length=50, choices=MED_SUB_CAT, default=MED_SUB_CAT)
    if category_set == 'Fitness':
        sub_categories = models.CharField(max_length=50, choices=FIT_SUB_CAT, default=MED_SUB_CAT)
    if category_set == 'Futbal':
        sub_categories = models.CharField(max_length=50, choices=FUT_SUB_CAT, default=MED_SUB_CAT)
    if category_set == 'Hockey':
        sub_categories = models.CharField(max_length=50, choices=HKY_SUB_CAT, default=MED_SUB_CAT)
    if category_set == 'Basketball':
        sub_categories = models.CharField(max_length=50, choices=BSK_SUB_CAT, default=MED_SUB_CAT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# ====== POST CLASSES ==========

class Drill(models.Model):
    # MED_TOOLS = [
    # ]

    # FIT_TOOLS = [
    # ]

    FUT_TOOLS = [
        ('ball', 'images/futball.jpeg'),
        ('cone', 'images/cone.jpeg'),
        ('attack', 'images/attack.jpeg'),
        ('midfiler', 'images/midfielder.jpeg'),
        ('defender', 'images/defender.jpeg'),
        ('goalkeeper', 'images/goalkeper.jpeg'),
        ('sweeper', 'images/sweeper.jpeg'),
        ('x', 'images/x.jpeg'),
        ('o', 'images/o.jpeg'),
    ]
    HKY_TOOLS = [
        ('puck', 'images/puck.jpeg'),
        ('cone', 'images/cone.jpeg'),
        ('pad', 'images/pad.jpeg'),
        ('attk_tri', 'images/attacktriangle.jpeg'),
        ('forward', 'images/forward.jpeg'),
        ('defender', 'images/defender.jpeg'),
        ('goalkeeper', 'images/goalkeper.jpeg'),
        ('x', 'images/x.jpeg'),
        ('o', 'images/o.jpeg'),
    ]
    category=Category.category
    if category == 'Medical':
        whiteboard_background_image='images/blank_board.jpeg'
    if category == 'Fitness':
        whiteboard_background_image='images/blank_board.jpeg'
    if category == 'Futball':
        whiteboard_background_image='images/soccer_field.jpeg'
        tools=FUT_TOOLS[1]
    if category == 'Hockey':
        whiteboard_background_image='images/hockey_board,jpeg'
        tools=HKY_TOOLS[1]
    sub_categories_defined=models.ManyToManyField(SubCategory, related_name="drill")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PracticePlan(models.Model):
    category = Category.category
    drill=models.ManyToManyField(Drill, related_name='practice_plan')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    category=models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
    sub_categories=models.ManyToManyField(SubCategory, related_name="post")
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/post/<category>/", null=True)
    # files=models.FileField()
    post_type=models.ForeignKey(PostType, related_name='post', on_delete=models.CASCADE)
    if post_type == 'Drill':
        post_type = models.ForeignKey(Drill, related_name='post', on_delete=models.CASCADE)
    if post_type == 'Practice Plan':
        post_type = PracticePlan()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

