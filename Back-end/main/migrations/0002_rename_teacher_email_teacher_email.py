# Generated by Django 4.1.5 on 2023-02-26 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_email',
            new_name='email',
        ),
    ]
