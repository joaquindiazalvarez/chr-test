from django.shortcuts import render
from .models import Network, Station
from django.http.response import HttpResponse
from .models import Network, Station
import json
import requests

def retrieve(request):
    """
    """
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    if response.status_code == 200:
        retrieved = json.loads(response.text)
        data = retrieved['network']
        network = Network()
        network.network_id = data['id']
        network.name = data['name']
        network.company = data['company']
        network.href = data['href']
        network.gbfs_href = data['gbfs_href']
        network.location_city = data['location']['city']
        network.location_country = data['location']['country']
        network.location_latitude = data['location']['latitude']
        network.location_longitude = data['location']['longitude']
        network.save()

        stations = data['stations']

        for station in stations:
            new_station = Station()
            new_station.station_id = station['id']
            new_station.name = station['name']
            new_station.timestamp = station['timestamp']
            new_station.longitude = station['longitude']
            new_station.latitude = station['latitude']
            new_station.free_bikes = station['free_bikes']
            new_station.empty_slots = station['empty_slots']
            new_station.network = network
            new_station.save()
    return HttpResponse("Ok")