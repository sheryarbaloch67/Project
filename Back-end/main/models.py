from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, check_password


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, null=True)
    scale = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_teacher(sender, instance, created, **kwargs):
    if created:
        Teacher.objects.create(
            user=instance,
            designation='',
            scale=0
        )


@receiver(post_save, sender=User)
def save_teacher(sender, instance, **kwargs):
    try:
        instance.teacher.save()
    except Teacher.DoesNotExist:
        pass


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    credit_hours = models.IntegerField(default=3)
    discipline = models.CharField(max_length=5, default='BSCS')
    semester = models.SmallIntegerField(default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255, null=True)
    date_delivered = models.DateField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('lecture_id', 'course')


class Question(models.Model):
    s_no = models.AutoField(primary_key=True)
    question = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    correct_option = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('s_no', 'lecture')
