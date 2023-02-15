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
        data = json.loads(response.text)
        network = Network()
        network.network_id = data['id']
        network.name = data['name']
        network.company = data['company']
        network.href = data['href']
        network.gbfs_href = data['gbfs_href']
        network.location_city = data['location_city']
        network.location_country = data['location_country']
        network.location_latitude = data['location_latitude']
        network.location_longitude = data['location_longitude']
        network.save()

        stations = data['stations']
        for i in range(len(stations)):
            
            stations[i]

    return HttpResponse("Ok")