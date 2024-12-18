# Generated by Django 5.1.2 on 2024-11-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option3',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=101),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=101),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=101),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=101),
        ),
    ]
