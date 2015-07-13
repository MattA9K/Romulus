from django.db import models
from time import time


class ContactForm(models.Model):
    Title = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Body = models.TextField()
    birth_date = models.DateTimeField(default=datetime.datetime.now)

class PageHit(models.Model):
    pagehit_time = models.DateTimeField(default=datetime.datetime.now)
    remote_address = models.CharField(max_length=150)
    user_agent = models.CharField(max_length=150)
    referer = models.CharField(max_length=150)