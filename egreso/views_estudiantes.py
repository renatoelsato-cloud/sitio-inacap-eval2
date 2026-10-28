from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EstudianteForm
from .models import Estudiante


@login_required
@permission_required("egreso.view_estudiante", raise_exception=True)
def estudiante_listado(request):
    q = request.GET.get("q", "").strip()
    estudiantes = Estudiante.objects.all()
    if q:
        estudiantes = estudiantes.filter(Q(nombre__icontains=q) | Q(rut__icontains=q))
    return render(request, "egreso/estudiante_listado.html", {"estudiantes": estudiantes, "q": q})


@login_required
@permission_required("egreso.add_estudiante", raise_exception=True)
def estudiante_crear(request):
    form = EstudianteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Estudiante creado correctamente.")
        return redirect("estudiante_listado")
    return render(request, "egreso/estudiante_form.html", {"form": form, "titulo": "Agregar estudiante"})


@login_required
@permission_required("egreso.change_estudiante", raise_exception=True)
def estudiante_editar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    form = EstudianteForm(request.POST or None, instance=estudiante)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Estudiante modificado correctamente.")
        return redirect("estudiante_listado")
    return render(request, "egreso/estudiante_form.html", {"form": form, "titulo": "Modificar estudiante"})


@login_required
@permission_required("egreso.delete_estudiante", raise_exception=True)
def estudiante_eliminar(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        estudiante.delete()
        messages.success(request, "Estudiante eliminado correctamente.")
        return redirect("estudiante_listado")
    return render(request, "egreso/estudiante_confirmar_eliminar.html", {"estudiante": estudiante})
