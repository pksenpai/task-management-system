from django.urls import path
from .views import *


app_name = 'tasks'
urlpatterns = [
    path('<int:id>/all/', all_tasks, name='all'),
    path('<int:id>/done/', done_tasks, name='done'),
    path('<int:id>/pending/', pending_tasks, name='pending'),
    
    path('<int:id>/add/', add_task, name='add'),
    path('<int:id>/update/', update_task, name='update'),
    path('<int:id>/remove/', remove_task, name='remove'),
]

