from django.urls import path
from .views import *


app_name = 'tasks'
urlpatterns = [
    path('<int:id>/all/', all_tasks, name='all'),
    path('<int:id>/done/', done_tasks, name='done'),
    path('<int:id>/pending/', pending_tasks, name='pending'),
    path('<int:id>/mytasks/', own_tasks, name='mytasks'),
    
    path('<int:wid>/update/<int:tid>/', task_update, name='update'),
    path('<int:wid>/delete/<int:tid>/', task_delete, name='delete'),
    path('<int:wid>/complete/<int:tid>/', task_complete, name='complete'),
    
    path('all-tasks-of-mine/', atom, name='atom'),
]

