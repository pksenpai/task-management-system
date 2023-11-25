from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *


"""\________________________SignUp________________________/"""

def signup(request):
    if request.user.is_authenticated:
        return redirect('/workspace')
    
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/workspace')
        else:
            print(form.errors)

    context = {
        'footer': True,
        'form': form,
    }
    template = 'signup.html'
    return render(request, template, context=context)

"""\________________________Login________________________/"""

# def login(request):
#     template = 'login.html'
#     return render(request, template, {'footer': True})

