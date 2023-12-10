from django.db import models
from django.utils import timezone
# Create your models here.
class Complains(models.Model):
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    complain = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)