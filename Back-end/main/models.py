import django
from django.db import models
from django.conf import settings

#django.conf.settings.configure()

installed_apps = settings.INSTALLED_APPS

# Create your models here.

# class Discipline(models.Model):
#     discipline_id = models.AutoField(primary_key=True)
#     discipline_name = models.CharField(max_length=100)
#     acronym = models.CharField(max_length=20, null=True)

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True)
    teacher_email = models.EmailField(max_length=100, unique=True)
    scale = models.IntegerField(null=True)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    credit_hours = models.IntegerField()
    discipline = models.CharField(max_length=5)
    semester = models.SmallIntegerField()
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255, null=True)
    date_delivered = models.DateField(null=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('lecture_id', 'course_id')

class Question(models.Model):
    s_no = models.AutoField(primary_key=True)
    question = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    correct_option = models.TextField()
    lecture_id = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('s_no', 'lecture_id')