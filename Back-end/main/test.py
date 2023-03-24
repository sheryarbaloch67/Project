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

# Create your views here.

def cover(request):
    return render(request, 'index.html')


def test(request):
    teachers = Teacher.objects.all
    return render(request, 'test.html', {'all':teachers})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomAuthBackend().authenticate(request=request, email=email, password=password)
            print(user)
            if user is not None:
                print('succeed')
                login(request, user)
                # next_page = request.GET.get('next', 'dashboard')
                # if next_page:
                #     return redirect(next_page)
                # else:
                print(request.user)
                print(request.session)
                return redirect(dashboard)
            else:
                print('fail')
                return render(request, 'signin.html', {'form': form, 'error': 'Invalid login'})
        else:
            return render(request, 'signin.html', {'form': form, 'error': 'Invalid form data'})

    else:
        form = LoginForm()
        return render(request, 'signin.html', {'form': form})


# @login_required(login_url='signin/')
def dashboard(request):
    print('test')
    print(request.user)
    # # return render(request, 'dashboard.html')
    # if request.user.is_authenticated:
    #     print('In the if')
    #     # Render the dashboard page
    return render(request, 'dashboard.html')
    # else:
    #     print('in the else')
    #     # Redirect to the login page
    #     return redirect('signin')










    # froms.py file code

from django import forms
from .models import *

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)