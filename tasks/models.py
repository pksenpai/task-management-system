from django.db import models


COLOR_TASKS = [
    ('#FFFFFF', 'white'),
    ('#FF0000', 'Red'),
    ('#0000FF', 'Blue'),	
    ('#AAFF00', 'Green Bright'),
    ('#90EE90', 'Green Light'),
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
    
    # RELATIONS...............................
    workspace  = models.ForeignKey("workspaces.Workspace", on_delete=models.CASCADE, related_name='task')

    def __str__(self) -> str:
        return self.title

