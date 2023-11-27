from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *

"""\________________________SignUp________________________/"""

def signup(request):
    if request.user.is_authenticated:
        return redirect('/workspace/')
    
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 
                f'your Account created Successfully!'
            )
            messages.success(
                request, 
                f'Welcome {username} :3'
            )
            return redirect("/accounts/login/")    
        
    context = {
        'footer': True,
        'form': form,
    }
    template = 'signup.html'
    return render(request, template, context)
    
    
"""\________________________Login________________________/"""

def login_view(request):
    if not request.user.is_authenticated :
        form = LoginForm()
        print(form)
        template = 'login.html'
        context = {
            'footer': True,
            'form': form,
        }
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/workspace/')
                else:
                    return render(request, template, context)
        
        return render(request, template, context)
    else:
        return redirect('/')


"""\________________________Logout________________________/"""

@login_required
def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

