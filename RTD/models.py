from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
import datetime

class Energy(models.Model):
    idd = models.IntegerField()
    timestamp = models.CharField(max_length=250)
    source = models.CharField(max_length=250)
    data = models.FloatField()
    time_string = models.CharField(max_length=250)
    @property
    def time_obj(self):
        return datetime.datetime.strptime(self.time_string, '%m/%d/%Y, %H:%M:%S')

    def __str__(self):
        return str(self.idd) + " " + self.source + ' ' + self.time_string + ' ' + str(self.data) + self.timestamp