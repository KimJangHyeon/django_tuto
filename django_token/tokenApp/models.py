from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.
class Users(models.Model):
    uid = models.CharField(max_length=256)
    pw = models.CharField(max_length=32)
    contents = models.TextField()

    def __str__(self):
        return self.uid

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)