# Create your views here.
import requests
from django.shortcuts import render
from .models import Resultado

def buscar(request):
    if 'q' in request.GET:
        query = request.GET['q']
        url = f'https://api.example.com/buscar?q={query}'
        response = requests.get(url)
        resultados = response.json()

        for resultado in resultados:
            Resultado.objects.create(
                titulo=resultado['titulo'],
                descripcion=resultado['descripcion']
            )

    resultados_guardados = Resultado.objects.all()

    return render(request, 'buscar.html', {'resultados': resultados_guardados})
