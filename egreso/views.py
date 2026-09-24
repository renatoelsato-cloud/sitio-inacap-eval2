from django.shortcuts import render
from .models import Competencia, Nota


def perfil(request):
    return render(request, 'egreso/perfil.html')


def competencias(request):
    lista_competencias = Competencia.objects.all()

    contexto = {
        'competencias': lista_competencias,
    }
    return render(request, 'egreso/competencias.html', contexto)


def notas(request):
    lista_notas = Nota.objects.select_related('estudiante', 'asignatura').all()

    contexto = {
        'notas': lista_notas,
    }
    return render(request, 'egreso/notas.html', contexto)
