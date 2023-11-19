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

    class Meta:
        verbose_name        = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.username} - {self.first_name.title()} {self.last_name.title()}" 

class Category(models.Model): 
    title = models.CharField(max_length=50)
    
class Tag(models.Model):
    title = models.CharField(max_length=50, choices=TAG_TITLES)
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    member_count = models.IntegerField()
    membership = models.ManyToManyField(User, related_name='group')
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    color = models.CharField(max_length=8, choices=COLOR_TASKS, default='white')
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='task')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='task')
    
