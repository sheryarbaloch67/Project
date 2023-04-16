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

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['topic', 'date_delivered']
        widgets = {
            'topic': forms.TextInput(attrs={'placeholder': 'e.g; Arrays & Strings'}),
            'date_delivered': forms.DateInput(attrs={'type': 'date'})
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option']
        widgets = {
            'question': forms.TextInput(attrs={'placeholder': 'Title of the question.....','id':'ques'}),
            'option_1': forms.TextInput(attrs={'placeholder': 'Option 1','id':'1'}),
            'option_2': forms.TextInput(attrs={'placeholder': 'Option 2','id':'2'}),
            'option_3': forms.TextInput(attrs={'placeholder': 'Option 3','id':'3'}),
            'option_4': forms.TextInput(attrs={'placeholder': 'Option 4','id':'4'}),
            'correct_option': forms.TextInput(attrs={'placeholder': 'Correct Option','id':'correct'}),
        }
