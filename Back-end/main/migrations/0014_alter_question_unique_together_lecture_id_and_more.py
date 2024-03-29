# Generated by Django 4.1.7 on 2023-04-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_course_credit_hours_alter_course_semester'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='question',
            name='lecture',
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lecture',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
