from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    typology = models.CharField(max_length=20)
    titular = models.CharField(max_length=200)
    investment = models.FloatField()
    date = models.CharField(max_length=20)
    state = models.CharField(max_length=200)