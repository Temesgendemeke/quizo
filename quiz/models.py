from sys import maxsize
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question}"


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} "


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField()
    subject = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} quiz takend by {self.user}"
