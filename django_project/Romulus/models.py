from django.db import models


class ContactForm(models.Model):
    Title = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Body = models.TextField()
    Date_created = models.DateTimeField(auto_now_add=True, blank=True)

class PageHit(models.Model):
    pagehit_time = models.DateTimeField(auto_now_add=True, blank=True)
    remote_address = models.CharField(max_length=150)
    user_agent = models.CharField(max_length=150)
    referer = models.CharField(max_length=150)