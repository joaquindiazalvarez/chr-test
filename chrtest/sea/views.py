from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import requests
from bs4 import BeautifulSoup
# Create your views here.
def retrieve(request):

    url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

    response = requests.post(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    row_array = []

    for row in rows:
        cells = row.find_all("td")
        cell_array = []
        for cell in cells:
            data = cell.text.strip()
            cell_array.append(data)
        
        row_array.append(cell_array)

    """ for row in row_array:
        new_project = Project()
        new_project.name = row[0]
        new_project.type = row[1]
        new_project.region = row[2]
        new_project.typology = row[3]
        new_project.titular = row[4]
        new_project.inversion = row[5]
        new_project.date = row[6]
        new_project.state = row[7]
        new_project.save() """
    return HttpResponse(row_array)