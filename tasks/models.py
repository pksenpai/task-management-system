from django.contrib.auth.models import AbstractUser
from django.db import models


CATEGORY_CHOICES = [
    ('EDU', 'Education'),
    ('IT', 'Engineering-IT'),
    ('MRK', 'Marketing'),	
    ('OPR', 'Operations'),
    ('SMB', 'Small Business'),
    ('HRS', 'Human Resources'),
    ('CRM', 'Sales CRM'),
    ('SCL', 'School'),
    ('HSW', 'Housework'),
    ('PRS', 'Personal Stuff'),
]

COLOR_TASKS = [
    ('#FFFFFF', 'white'),
    ('#FF0000', 'Red'),
    ('#0000FF', 'Blue'),	
    ('#AAFF00', 'Green Bright'),
    ('#90EE90', 'Green Light'),
]

class User(AbstractUser):
    last_login       = None
    groups           = None
    user_permissions = None
    
    class Meta:
        verbose_name = 'user'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Category(models.Model): 
    title = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='School')
    
class Tag(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
    

class Workspace(models.Model): # add HOST later
    # MAIN..............................
    name = models.CharField(max_length=100)

    # EXTRA..............................
    member_count = models.IntegerField(default=1)
    public       = models.BooleanField(default=False)
    
    # RELATIONS.........................
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag        = models.ManyToManyField(Tag)
    members    = models.ManyToManyField(User, related_name='workspace')
    
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
    workspace  = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='task')

    def __str__(self) -> str:
        return self.title

