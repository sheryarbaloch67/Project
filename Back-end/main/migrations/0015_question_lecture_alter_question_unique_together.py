# Generated by Django 4.1.7 on 2023-04-16 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_question_unique_together_lecture_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='lecture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.lecture'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('s_no', 'lecture')},
        ),
    ]