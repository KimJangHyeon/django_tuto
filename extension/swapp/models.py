from django.db import models
from datetime import datetime
# Create your models here.

class TodoList(models.Model):
  lid = models.AutoField(primary_key=True)
  date = models.DateTimeField(default=datetime.now())
  title = models.CharField(max_length=128, null=False)
  context = models.TextField(null=True)

class Memo(models.Model):
  mid = models.AutoField(primary_key=True)
  context = models.TextField(null=True)

class Time(models.Model):
  time_zone = models.IntegerField()



