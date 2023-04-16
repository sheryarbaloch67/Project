from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [TeacherInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Question)