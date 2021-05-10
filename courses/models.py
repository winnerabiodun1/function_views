from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=75, null=False, blank=False)
    password = models.CharField(max_length=512, null=False, blank=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
