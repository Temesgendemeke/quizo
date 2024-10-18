from django.contrib import admin
from .models import Subject, Question, Result, Quiz

# Register your models here.
admin.site.register([Subject, Question, Result, Quiz])
