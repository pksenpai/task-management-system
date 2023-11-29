from django.contrib.auth.models import User
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

class Category(models.Model): 
    title = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    
    def __str__(self) -> str:
        return self.get_title_display() # show full title django-built-in method
    
class Tag(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
    

class Workspace(models.Model): 
    # MAIN..............................
    # host = models.CharField(max_length=150) # WHO Create Workspace with host permissions
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # EXTRA..............................
    member_count = models.IntegerField(default=1)
    public       = models.BooleanField(default=False)
    
    # RELATIONS.........................
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag        = models.ManyToManyField(Tag, related_name='workspace')
    members    = models.ManyToManyField(User, related_name='workspace')
    
    def __str__(self) -> str:
        return f"{self.name} -> count: {self.member_count} | members: {self.members}" 

