from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=80)
    region = models.CharField(max_length=80)
    typology = models.CharField(max_length=10)
    titular = models.CharField(max_length=80)
    inversion = models.IntegerField()
    date = models.CharField(max_length=10)
    state = models.CharField(max_length=80)