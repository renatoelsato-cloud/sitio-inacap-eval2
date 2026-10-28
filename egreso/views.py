from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Competencia, Estudiante, CampoLaboral, Nota


@login_required
def perfil(request):
    estudiantes = Estudiante.objects.all()
    campos_laborales = CampoLaboral.objects.select_related('estudiante').all()

    contexto = {
        'estudiantes': estudiantes,
        'campos_laborales': campos_laborales,
    }
    return render(request, 'egreso/perfil.html', contexto)


@login_required
def competencias(request):
    lista_competencias = Competencia.objects.all()

    contexto = {
        'competencias': lista_competencias,
    }
    return render(request, 'egreso/competencias.html', contexto)


@login_required
def notas(request):
    lista_notas = Nota.objects.select_related('estudiante', 'asignatura').all()

    contexto = {
        'notas': lista_notas,
    }
    return render(request, 'egreso/notas.html', contexto)

