# Generated by Django 4.1.5 on 2023-02-25 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=20)),
                ('credit_hours', models.IntegerField()),
                ('discipline', models.CharField(max_length=5)),
                ('semester', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('scale', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=255, null=True)),
                ('date_delivered', models.DateField(null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'unique_together': {('lecture_id', 'course_id')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option_1', models.TextField()),
                ('option_2', models.TextField()),
                ('option_3', models.TextField()),
                ('option_4', models.TextField()),
                ('correct_option', models.TextField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('lecture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.lecture')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'unique_together': {('s_no', 'lecture_id')},
            },
        ),
    ]
