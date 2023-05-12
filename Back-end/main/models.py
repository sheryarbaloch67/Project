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
    DISCIPLINE_CHOICES = (
        ('BSCS', 'BSCS'),
        ('BSSE', 'BSSE'),
        ('BSAI', 'BSAI'),
    )

    SEMESTER_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )

    CREDIT_CHOICES = (
        ('3', '3'),
        ('4', '4'),
    )

    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    credit_hours = models.CharField(max_length=5, choices=CREDIT_CHOICES, default='3')
    discipline = models.CharField(max_length=5, choices=DISCIPLINE_CHOICES, default='BSCS')
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES, default='1')
    # credit_hours = models.IntegerField(default=3)
    # discipline = models.CharField(max_length=5, default='BSCS')
    # semester = models.SmallIntegerField(default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Lecture(models.Model):
    lecture_id = models.IntegerField(default=1)
    topic = models.CharField(max_length=255, null=True)
    date_delivered = models.DateField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('lecture_id', 'course')

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set the lecture_id on creation, not update
            # Get the count of existing lectures for the course
            existing_count = Lecture.objects.filter(course=self.course).count()
            self.lecture_id = existing_count + 1
        super().save(*args, **kwargs)


class Question(models.Model):
    s_no = models.IntegerField(default=1)
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
        unique_together = ('s_no', 'lecture', 'course')

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set the s_no on creation, not update
            # Get the count of existing questions for the lecture
            existing_count = Question.objects.filter(lecture=self.lecture).count()
            self.s_no = existing_count + 1
        super().save(*args, **kwargs)
