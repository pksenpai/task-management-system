from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views # for login, logout, &... views


app_name = 'users'
urlpatterns = [
    # path('', signup, name='signup'),
    path('signup/', signup, name='signup'),
    # path(
    #     'login/', 
    #     auth_views.LoginView.as_view(
    #             template_name='login.html'
    #         ), 
    #     name='login'
    # ),
    path('login/', login_view, name='login'),
    path(
        'logout/', 
        auth_views.LogoutView.as_view(), 
        name='logout'
    ),
]