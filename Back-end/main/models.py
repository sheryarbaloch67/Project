from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Teacher(models.Model):
    last_login = models.DateTimeField(auto_now=True)
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    designation = models.CharField(max_length=100, null=True)
    scale = models.IntegerField(null=True)

    def set_password(self, raw_password):
        """
        Set the password for this user to the given raw string.
        """
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Return True if the given raw string matches the stored hashed password.
        """
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.teacher_name


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