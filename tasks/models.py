from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from django.utils import timezone
from django.db import models


@property
def date_compare(self): # you still have time to do task
    return date.today() < self.date    
    
def date_validation(value):
    if value < timezone.now():
        raise ValidationError("Please enter a future date! :3") # ADD pop-up to say error NEW FEATURE <<<<
    
COLOR_TASKS = [
    ('dark', 'black'),
    ('secondry', 'gray'),
    ('light', 'light'),
    ('white', 'white'),
    ('warning', 'yellow'),
    ('danger', 'Red'),
    ('success', 'green'),
    ('info', 'teal'),	
    ('primary', 'Blue'),
]

class Task(models.Model):
    # MAIN...................................
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date    = models.DateTimeField(validators=[date_validation])
    status      = models.BooleanField(default=False)
    
    # PERMISSION..............................
    owner                   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner') # WHO Created task with owner permissions
    edit_task_permission    = models.ManyToManyField(User, blank=True, related_name='tutp')
    functor_task_permission = models.ManyToManyField(User, blank=True, related_name='tftp')
    
    # EXTRA...................................    
    hide  = models.BooleanField(default=False)
    force = models.BooleanField(default=False) # will be a feature ########## after beta version
    color = models.CharField(max_length=8, choices=COLOR_TASKS, default='white')
    
    # RELATIONS...............................
    workspace  = models.ForeignKey("workspaces.Workspace", on_delete=models.CASCADE, related_name='task')

    def __str__(self) -> str:
        return self.title

