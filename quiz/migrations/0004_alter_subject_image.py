# Generated by Django 5.1.2 on 2024-11-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_question_option3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
