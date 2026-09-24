import json
import requests
from django.shortcuts import render


def perfil(request):
    return render(request, 'egreso/perfil.html')


def competencias(request):
    with open('egreso/data/perfil.json', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    lista_competencias = datos['competencias']

    try:
        respuesta = requests.get('https://timeapi.io/api/time/current/zone?timeZone=America/Santiago', timeout=5)
        hora_completa = respuesta.json()['dateTime']
        hora_actual = hora_completa.split('.')[0].replace('T', ' ')
    except Exception:
        hora_actual = 'No disponible'

    contexto = {
        'competencias': lista_competencias,
        'hora_actual': hora_actual,
    }
    return render(request, 'egreso/competencias.html', contexto)