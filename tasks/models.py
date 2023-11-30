from django.contrib.auth.models import User
from django.db import models


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
    due_date    = models.DateTimeField()
    status      = models.BooleanField(default=False)
    
    # PERMISSION..............................
    owner                   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner') # WHO Created task with owner permissions
    edit_task_permission  = models.ManyToManyField(User, blank=True, related_name='tutp')
    functor_task_permission = models.ManyToManyField(User, blank=True, related_name='tftp')
    
    # EXTRA...................................    
    hide  = models.BooleanField(default=False)
    force = models.BooleanField(default=False)
    color = models.CharField(max_length=8, choices=COLOR_TASKS, default='white')
    
    # RELATIONS...............................
    workspace  = models.ForeignKey("workspaces.Workspace", on_delete=models.CASCADE, related_name='task')

    def __str__(self) -> str:
        return self.title

