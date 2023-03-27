# from django.contrib import admin
# from .models import Teacher

# # Register your models here.

# admin.site.register(Teacher)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# from .models import Teacher

# class TeacherInline(admin.StackedInline):
#     model = Teacher
#     can_delete = False

# class CustomUserAdmin(UserAdmin):
#     inlines = [TeacherInline]

#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         if not change:
#             Teacher.objects.create(
#                 user=obj,
#                 email=obj.email,
#             )

#     def save_related(self, request, form, formsets, change):
#         super().save_related(request, form, formsets, change)
#         if not change:
#             teacher = form.instance.teacher
#             teacher.user_id = form.instance.id
#             teacher.save()

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Teacher)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Teacher

class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [TeacherInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Teacher)