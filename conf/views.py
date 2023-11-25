from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


"""\_________________________HOME_________________________/"""

def home(request):
    template = "home.html"
    return render(request, template)

"""\_______________________EXTRA_______________________/"""

def sad(request):
    template = 'sadcat.html'
    return render(request, template)

