from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cover(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

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
