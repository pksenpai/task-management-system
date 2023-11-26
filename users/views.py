from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
from .models import *

"""\________________________SignUp________________________/"""

# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/workspace')
    
#     form = SignUpForm()
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             return redirect('/workspace')
#         else:
#             print(form.errors)

#     context = {
#         'footer': True,
#         'form': form,
#     }
#     template = 'signup.html'
#     return render(request, template, context=context)

def signup(request):
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
         
    return render(request, 'signup.html', {'form': form})
    
    
"""\________________________Login________________________/"""

def login_view(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'accounts/login.html')
            
        return render(request, 'accounts/login.html')
    else:
        return redirect('/')


