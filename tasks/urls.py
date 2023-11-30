from django.urls import path
from .views import *


app_name = 'tasks'
urlpatterns = [
    path('<int:id>/all/', all_tasks, name='all'),
    path('<int:id>/done/', done_tasks, name='done'),
    path('<int:id>/pending/', pending_tasks, name='pending'),
    path('<int:id>/mytasks/', own_tasks, name='mytasks'),
    
    path('<int:id>/update/', task_update, name='update'),
    path('<int:id>/delete/', task_delete, name='delete'),
]

