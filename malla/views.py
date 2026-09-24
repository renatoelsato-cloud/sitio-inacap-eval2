import json
from django.shortcuts import render


def inicio(request):
    return render(request, 'malla/inicio.html')


def listado(request):
    with open('malla/data/malla.json', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    semestres = datos['semestres']

    total_asignaturas = 0
    for semestre in semestres:
        total_asignaturas = total_asignaturas + len(semestre['asignaturas'])

    if total_asignaturas > 10:
        mensaje = 'Malla curricular con alta carga academica.'
    else:
        mensaje = 'Malla curricular con carga academica moderada.'

    contexto = {
        'semestres': semestres,
        'total_asignaturas': total_asignaturas,
        'mensaje': mensaje,
    }
    return render(request, 'malla/listado.html', contexto)