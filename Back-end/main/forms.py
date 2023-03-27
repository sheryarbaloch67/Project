from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *


class LoginForm(AuthenticationForm):
    pass


# class TeacherProfileForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = ('first_name', 'last_name', 'username', 'email', 'password', 'designation', 'scale')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Set initial values for the user fields
#         self.initial.update({
#             'first_name': self.instance.user.first_name,
#             'last_name': self.instance.user.last_name,
#             'username': self.instance.user.username,
#             'email': self.instance.user.email,
#             'password': self.instance.user.password,
#         })

#     def save(self, commit=True):
#         # Save the User and Teacher models
#         user = self.instance.user
#         user.username = self.cleaned_data['username']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()

#         teacher = super().save(commit=False)
#         teacher.teacher_name = self.cleaned_data['username']
#         teacher.save()
#         return teacher


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