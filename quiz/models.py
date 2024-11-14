from sys import maxsize
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.utils.choices import BlankChoiceIterator

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=101)
    image = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    question = models.CharField(max_length=101)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100, null=True, blank=True)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=101)

    def __str__(self):
        return f"{self.question}"


class Quiz(models.Model):
    title = models.CharField(max_length=101)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} "


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField()
    subject = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} quiz takend by {self.user}"
