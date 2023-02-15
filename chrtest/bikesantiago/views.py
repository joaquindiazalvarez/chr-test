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

        for i in range(len(stations)):
            new_station = Station()
            new_station.station_id = stations[i]['id']
            new_station.name = stations[i]['name']
            new_station.timestamp = stations[i]['timestamp']
            new_station.longitude = stations[i]['longitude']
            new_station.latitude = stations[i]['latitude']
            new_station.free_bikes = stations[i]['free_bikes']
            new_station.empty_slots = stations[i]['empty_slots']
            new_station.network = network
            new_station.save()
    return HttpResponse("Ok")