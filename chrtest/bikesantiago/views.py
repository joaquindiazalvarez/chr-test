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
    return HttpResponse("Ok")