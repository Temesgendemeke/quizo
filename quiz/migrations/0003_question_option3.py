# Generated by Django 5.1.2 on 2024-11-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_question_option3_alter_question_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
