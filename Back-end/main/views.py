from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# from main.Emailbackend import Emailbackend
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .custom_auth_backend import CustomAuthBackend

# Create your views here.

def cover(request):
    return render(request, 'index.html')


def test(request):
    teachers = Teacher.objects.all
    return render(request, 'test.html', {'all':teachers})

# def signup(request):
#     return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomAuthBackend().authenticate(request=request, email=email, password=password)
            print(user)
            if user!=None:
                login(request, user) 
                return redirect(dashboard)
            else:
                print(user)
                return render(request, 'signin.html', {'form': form, 'error': 'Invalid login'})
        else:
            return render(request, 'signin.html', {'form': form, 'error': 'Invalid form data'})

    else:
        form = LoginForm
        return render(request, 'signin.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def course(request):
    return render(request, 'add course.html')

def lecture(request):
    return render(request, 'add lecture.html')

def lectures(request):
    return render(request, 'all lectures.html')

def mcqs(request):
    return render(request, 'add mcqs.html')

def activity(request):
    return render(request, 'activity.html')
