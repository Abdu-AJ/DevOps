from django.db import models
from django.utils import timezone
from django.db.models import Manager

class Complains(models.Model):
    objects: Manager = models.Manager()
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    complain = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

class Daily_Usage(models.Model):
    objects: Manager = models.Manager()
    phonenumber = models.CharField(max_length=200)
    LocalSMSPricing = models.DecimalField(max_digits=10, decimal_places=2)
    GPRSPricing = models.DecimalField(max_digits=10, decimal_places=2)
    OffNetPricing = models.DecimalField(max_digits=10, decimal_places=2)
    IrishLandlinePricing = models.DecimalField(max_digits=10, decimal_places=2)
    InternationalCallPricing = models.DecimalField(max_digits=10, decimal_places=2)
    InternationalSMSPricing = models.DecimalField(max_digits=10, decimal_places=2)
    OnNetPricing = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    class Meta:
        unique_together = [['phonenumber', 'date']]
class Pricing (models.Model):
    LocalSMSPricing = models.DecimalField(max_digits=10, decimal_places=2)
    GPRSPricing = models.DecimalField(max_digits=10, decimal_places=2)
    OffNetPricing = models.DecimalField(max_digits=10, decimal_places=2)
    IrishLandlinePricing = models.DecimalField(max_digits=10, decimal_places=2)
    InternationalCallPricing = models.DecimalField(max_digits=10, decimal_places=2)
    InternationalSMSPricing = models.DecimalField(max_digits=10, decimal_places=2)
    OnNetPricing = models.DecimalField(max_digits=10, decimal_places=2)