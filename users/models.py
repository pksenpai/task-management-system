from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    last_login       = None
    groups           = None
    user_permissions = None
    
    class Meta:
        verbose_name = 'user'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

