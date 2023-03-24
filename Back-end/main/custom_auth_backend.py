from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Teacher

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            teacher = Teacher.objects.get(email=email)
        except Teacher.DoesNotExist:
            pass
            print(f"No teacher found with email {email}")
            return None
    
        print(f"Email provided by form: {email}, Password provided by form: {password}")
        print(f"Email fetched from database: {teacher.email}, Hashed Password fetched from database: {teacher.password}")
        if password == teacher.password:
            return teacher