from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=75)
    password = models.CharField(max_length=512)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
