from django.db import models
import users.models



class Post(models.Model):
    CATEGORIES = [
        ('MED', 'Medical'),
        ('FIT', 'Fitness'),
        ('FUT', 'Soccer'),
        ('HKY', 'Hockey'),
        ('BSK', 'Basketball'),
        ('AFB', 'Football'),
        ('RUG', 'Rugby'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORIES, default='All')

    MED_SUB_CAT = [
        ('ALL', 'All'),
        ('NUT', 'Nutrition'),
        ('CNC', 'Concussion'),
        ('IRH', 'Injury Rehabilitation'),
        ('SRB', 'Surgical Rehabilitation'),
        ('IPV', 'Injury Prevention'),
        ('MTH', 'Mental Health'),
    ]
    FIT_SUB_CAT = [
        ('ALL', 'All'),
        ('RVY', 'Recovery'),
        ('FLX', 'Flexibility'),
        ('MBT', 'Mobility'),
        ('VIS', 'Vision'),
        ('STG', 'Strength'),
        ('CON', 'Conditioning'),
        ('SPD', 'Speed'),
    ]
    FUT_SUB_CAT = [
        ('ALL', 'All'),
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
        ('ALL', 'All'),
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
        ('ALL', 'All'),
        ('DBL', 'Dribbling'),
        ('SHT', 'Shooting'),
        ('PSS', 'Passing'),
        ('DEF', 'Defensive'),
        ('OFF', 'Offensive'),
        ('MOV', 'Movement'),
    ]

    sub_cats = MED_SUB_CAT
    if category == 'Medical':
        # sub_categories = models.CharField(max_length=50, choices=MED_SUB_CAT, default="All")
        sub_cats = MED_SUB_CAT
    if category == 'Fitness':
        # sub_categories = models.CharField(max_length=50, choices=FIT_SUB_CAT)
        sub_cats = FIT_SUB_CAT
    if category == 'Soccer':
        # sub_categories = models.CharField(max_length=50, choices=FUT_SUB_CAT)
        sub_cats = FUT_SUB_CAT
    if category == 'Hockey':
        # sub_categories = models.CharField(max_length=50, choices=HKY_SUB_CAT)
        sub_cats = HKY_SUB_CAT
    if category == 'Basketball':
        # sub_categories = models.CharField(max_length=50, choices=BSK_SUB_CAT)
        sub_cats = BSK_SUB_CAT

    sub_categories = models.CharField(max_length=50, choices=sub_cats, default="All")
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(users.models.User, related_name="post", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/post/<post_type>/<category>/", null=True)
    # files = models.FileField()

    TYPES = [
        ('BLG', 'Blog'),
        ('DRL', 'Drill'),
        ('PRP', 'Practice Plan'),
    ]
    post_type = models.CharField(max_length=100, choices=TYPES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at', 'post_type', 'category', 'sub_categories', 'title', 'description', 'user', 'image')

    def __str__(self):
        return self.title

