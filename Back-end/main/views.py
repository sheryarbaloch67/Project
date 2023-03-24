from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# from main.Emailbackend import Emailbackend
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .custom_auth_backend import CustomAuthBackend
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def cover(request):
    return render(request, 'index.html')


def test(request):
    teachers = Teacher.objects.all
    return render(request, 'test.html', {'all':teachers})


def signin(request):
    if request.method == "POST":
        print('in the form')
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            print('is valid')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect(dashboard)
            else:
                return render(request, 'signin.html', {'form': form, 'error': 'Invalid login'})
        else:
            return render(request, 'signin.html', {'form': form, 'error': 'Invalid form data'})

    else:
        form = LoginForm()
        return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin/')

@login_required(login_url='signin/')
def dashboard(request):
    print('test')
    print(request.user)
    return render(request, 'dashboard.html')


@login_required(login_url='signin/')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='signin/')
def course(request):
    return render(request, 'add course.html')


@login_required(login_url='signin/')
def lecture(request):
    return render(request, 'add lecture.html')


@login_required(login_url='signin/')
def lectures(request):
    return render(request, 'all lectures.html')


@login_required(login_url='signin/')
def mcqs(request):
    return render(request, 'add mcqs.html')


@login_required(login_url='signin/')
def activity(request):
    return render(request, 'activity.html')
