from django.db import models
from django.utils import timezone
from django.db.models import Manager

class Complains(models.Model):
    objects: Manager = models.Manager()  # Explicitly declare the manager for type hinting
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    complain = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)