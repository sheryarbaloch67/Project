# Generated by Django 4.1.7 on 2023-05-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_course_credit_hours_alter_course_discipline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credit_hours',
            field=models.CharField(choices=[('3', '3'), ('4', '4')], default='3', max_length=5),
        ),
        migrations.AlterField(
            model_name='course',
            name='discipline',
            field=models.CharField(choices=[('BSCS', 'BSCS'), ('BSSE', 'BSSE'), ('BSAI', 'BSAI')], default='BSCS', max_length=5),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=5),
        ),
    ]
