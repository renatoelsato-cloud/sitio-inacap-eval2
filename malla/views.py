from django.shortcuts import render
from .models import Semestre


def inicio(request):
    return render(request, 'malla/inicio.html')


def listado(request):
    semestres = Semestre.objects.prefetch_related('asignaturas').all()

    total_asignaturas = 0
    for semestre in semestres:
        total_asignaturas = total_asignaturas + semestre.asignaturas.count()

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
