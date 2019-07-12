from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Energy(models.Model):
    idd = models.IntegerField()
    timestamp = models.IntegerField()
    source = models.CharField(max_length=250)
    data = models.FloatField()