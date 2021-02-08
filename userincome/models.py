from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now


class UserIncome(models.Model):
    date = models.DateField(default=now)
    amount = models.FloatField()
    source = models.CharField(max_length=266)
    description = models.TextField()
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.source

    class Meta:
        ordering = ['-date']


class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name