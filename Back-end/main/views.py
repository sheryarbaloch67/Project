from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def cover(request):
    return render(request, 'index.html')


def test(request):
    teachers = Teacher.objects.all
    return render(request, 'test.html', {'all':teachers})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
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
    if hasattr(request.user, 'teacher'):
        courses = Course.objects.filter(teacher=request.user.teacher)
        context = {
            'courses': courses,
        }
    return render(request, 'dashboard.html', context)


@login_required(login_url='signin/')
def profile(request):
    user_form = UserUpdateForm(instance=request.user)
    teacher_form = TeacherProfileForm(instance=request.user.teacher)
    password_form = PasswordChangeForm(request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        teacher_form = TeacherProfileForm(request.POST, instance=request.user.teacher)
        password_form = PasswordChangeForm(request.user, request.POST)
        
        if user_form.is_valid() and teacher_form.is_valid() and password_form.is_valid():
            print('In the if')
            user_form.save()
            teacher_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user) # Important!
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'There was an error updating your profile. Please try again.')
    
    context = {
        'user_form': user_form,
        'teacher_form': teacher_form,
        'password_form': password_form,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='signin/')
def course(request):
    if hasattr(request.user, 'teacher'):
        if request.method == 'POST':
            form = CourseForm(request.POST)
            if form.is_valid():
                print('course form is valid')
                course = form.save(commit=False)
                course.teacher = request.user.teacher
                course.save()
                return redirect('dashboard')
        else:
            print('in the course')
            form = CourseForm()
        context = {
            'form': form,
        }
    return render(request, 'add course.html', context)


@login_required(login_url='signin/')
def lectures(request):
    return render(request, 'all lectures.html')


@login_required(login_url='signin/')
def lecture(request):
    return render(request, 'add lecture.html')


@login_required(login_url='signin/')
def mcqs(request):
    return render(request, 'add mcqs.html')


@login_required(login_url='signin/')
def activity(request):
    return render(request, 'activity.html')
