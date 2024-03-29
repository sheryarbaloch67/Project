# Generated by Django 4.1.7 on 2023-03-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_course_teacher_lecture_teacher_question_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit_hours',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='discipline',
            field=models.CharField(default='BSCS', max_length=5),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.SmallIntegerField(default=1),
        ),
    ]
