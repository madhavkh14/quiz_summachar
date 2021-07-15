from django.db import models
from django.contrib.auth.models import User
import jsonfield

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField(blank = True, null = True)
    end_time = models.DateTimeField(blank = True, null = True)
    question = models.ManyToManyField("Question",blank=True)

    def __str__(self):
        return str(self.title)

    def status(self, time):
        if self.end_time > time and self.start_time < time:
            return "live"
        elif self.end_time < time and self.end_time > self.start_time:
            return "past"
        elif self.start_time > time:
            return "upcoming"


class Question(models.Model):
    TYPES = {
			('MCQ', 'MCQ'),
            ('Text', 'Text'),
    }

    desc = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPES, default='MCQ')
    option = jsonfield.JSONField(blank=True, null=True)
    text = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return str(self.desc)

class QuizResponse(models.Model):
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    response = jsonfield.JSONField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)