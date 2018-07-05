from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
	event_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	text = models.TextField()


