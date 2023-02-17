from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Project
from bs4 import BeautifulSoup
import requests
# Create your views here.
def retrieve(request):
    page = 1
    row_array = []
    while True:
        url = f"https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual={page}"

        response = requests.post(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table")
        if not table:
            break
        rows = table.find_all("tr")

        for row in rows:
            cells = row.find_all("td")
            cell_array = []
            for cell in cells:
                data = cell.text.strip()
                if data != "":
                    cell_array.append(data)
            if len(cell_array) > 0: 
                row_array.append(cell_array)

        page += 1
    result = {"result": row_array}
    return JsonResponse(result)

"""        for row in row_array:
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

"""