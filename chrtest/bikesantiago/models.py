from django.db import models

# Create your models here.
class Network(models.Model):
    network_id = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    href = models.CharField(max_length=120)
    gbfs_href = models.CharField(max_length=120)
    location_city = models.CharField(max_length=80)
    location_country = models.CharField(max_length=80)
    location_latitude = models.IntegerField()
    location_longitude = models.IntegerField()

class Station(models.Model):
    station_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    timestamp = models.CharField(max_length=120)
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    free_bikes = models.IntegerField()
    empty_slots = models.IntegerField()
    network = models.ForeignKey(Network, on_delete=models.CASCADE)