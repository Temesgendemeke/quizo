# Generated by Django 5.1.1 on 2024-10-18 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_result_quiz_alter_quiz_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz'),
        ),
    ]