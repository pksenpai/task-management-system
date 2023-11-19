from django.db import models


class Category(models.Model): 
    name = models.CharField(max_length=50)
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeFiled()
    status = '?'
    tag = '?'
    public = models.BooleanFiled(default=False)
    category = models.ForeginKeyField(Category, on_delete=models.CASE_CADE)

class Tag(models.Model):
    task = models.ManyToManyField(Task, on_delete=models.CASE_CADE)

