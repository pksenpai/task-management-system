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
    
    # EXTRA...................................    
    hide  = models.BooleanField(default=False)
    color = models.CharField(max_length=8, choices=COLOR_TASKS, default='white')
    # add force task
    # owner
    
    # RELATIONS...............................
    workspace  = models.ForeignKey("workspaces.Workspace", on_delete=models.CASCADE, related_name='task')

    def __str__(self) -> str:
        return self.title

