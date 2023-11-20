from django.contrib.auth.models import AbstractUser
from django.db import models


TAG_TITLES = [ 
    ('D', 'DONE!'),
    ('I', 'IN PROGRESS'),
    ('P', 'PENDING...'),
    ('T', 'TO DO'),
]

COLOR_TASKS = [
    ('#FFFFFF', 'white'),
    ('#FF0000', 'Red'),
    ('#0000FF', 'Blue'),	
    ('#AAFF00', 'Green Bright'),
    ('#90EE90', 'Green Light'),
]

class User(AbstractUser):
    last_login = None
    groups = None
    user_permissions = None
    
    class Meta:
        verbose_name = 'user'
    
    
class Category(models.Model): 
    title = models.CharField(max_length=50)
    
class Tag(models.Model):
    title = models.CharField(max_length=50, choices=TAG_TITLES)

class Workspace(models.Model):
    # MAIN..............................
    name = models.CharField(max_length=100)

    # EXTRA..............................
    member_count = models.IntegerField(default=1)
    public = models.BooleanField(default=False)
    
    # RELATIONS.........................
    members = models.ManyToManyField(User, related_name='memberships')
    
    def __str__(self) -> str:
        return f"{self.name} -> count: {self.member_count} | members: {self.members}" 

class Task(models.Model):
    # MAIN...................................
    title       = models.CharField(max_length=200)
    description = models.TextField()
    due_date    = models.DateTimeField()
    status      = models.BooleanField(default=False)
    
    # EXTRA...................................    
    hide  = models.BooleanField(default=False)
    color = models.CharField(max_length=8, choices=COLOR_TASKS, default='white')
    
    # RELATIONS...............................
    tag        = models.ManyToManyField(Tag)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    workspace  = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='task')

    def __str__(self) -> str:
        return self.title

