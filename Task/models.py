from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    username = models.TextField()
    password = models.TextField()

class Task(models.Model):
    taskName = models.TextField(default=None)
    description = models.TextField(default=None)
    currentlyWorking = models.BooleanField(default=False)
    totaltime = models.DurationField(default=datetime.timedelta)
    startedAt = models.DateTimeField(auto_now_add=True)
    userReference = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
