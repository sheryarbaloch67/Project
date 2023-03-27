from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *


class LoginForm(AuthenticationForm):
    pass


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['designation', 'scale']

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'credit_hours', 'discipline', 'semester']
        labels = {
            'course_name': 'Course Title',
            'course_code': 'Course Code',
            'credit_hours': 'Credit Hours',
            'discipline': 'Discipline',
            'semester': 'Semester',
        }