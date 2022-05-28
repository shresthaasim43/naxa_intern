from operator import mod
from statistics import mode
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_logged_id = models.BooleanField(default = False)

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default = False)
    assignee_id = models.IntegerField()
    supervisor_id = models.IntegerField()

class Attendence(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    attendence_time = models.DateTimeField()