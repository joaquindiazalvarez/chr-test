from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from bs4 import BeautifulSoup
import requests
# Create your views here.
def retrieve(request):
    page = 1
    while True:
        url = f"https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual={page}"

        response = requests.post(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table")
        if not table:
            break
        rows = table.find_all("tr")

        row_array = []

        for row in rows:
            cells = row.find_all("td")
            cell_array = []
            for cell in cells:
                data = cell.text.strip()
                cell_array.append(data)
            
            row_array.append(cell_array)

        row_array = row_array[2:]

        for row in row_array:
            new_project = Project()
            new_project.name = row[1]
            new_project.type = row[2]
            new_project.region = row[3]
            new_project.typology = row[4]
            new_project.titular = row[5]
            new_project.investment = float(row[6].replace('.','').replace(',', '.'))
            new_project.date = row[7]
            new_project.state = row[8]
            new_project.save()
        page += 1
    return HttpResponse("Ok")