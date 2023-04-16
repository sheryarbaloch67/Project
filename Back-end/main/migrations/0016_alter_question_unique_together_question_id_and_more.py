# Generated by Django 4.1.7 on 2023-04-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_question_lecture_alter_question_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='question',
            name='s_no',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('s_no', 'lecture', 'course')},
        ),
    ]