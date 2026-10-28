from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q, ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AsignaturaForm
from .models import Asignatura


@login_required
@permission_required("malla.view_asignatura", raise_exception=True)
def asignatura_listado(request):
    q = request.GET.get("q", "").strip()
    asignaturas = Asignatura.objects.select_related("semestre").all()
    if q:
        asignaturas = asignaturas.filter(Q(nombre__icontains=q) | Q(codigo__icontains=q))
    return render(request, "malla/asignatura_listado.html", {"asignaturas": asignaturas, "q": q})


@login_required
@permission_required("malla.add_asignatura", raise_exception=True)
def asignatura_crear(request):
    form = AsignaturaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Asignatura creada correctamente.")
        return redirect("asignatura_listado")
    return render(request, "malla/asignatura_form.html", {"form": form, "titulo": "Agregar asignatura"})


@login_required
@permission_required("malla.change_asignatura", raise_exception=True)
def asignatura_editar(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    form = AsignaturaForm(request.POST or None, instance=asignatura)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Asignatura modificada correctamente.")
        return redirect("asignatura_listado")
    return render(request, "malla/asignatura_form.html", {"form": form, "titulo": "Modificar asignatura"})


@login_required
@permission_required("malla.delete_asignatura", raise_exception=True)
def asignatura_eliminar(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    if request.method == "POST":
        try:
            asignatura.delete()
            messages.success(request, "Asignatura eliminada correctamente.")
        except ProtectedError:
            messages.error(request, "No se puede eliminar: la asignatura tiene notas registradas.")
        return redirect("asignatura_listado")
    return render(request, "malla/asignatura_confirmar_eliminar.html", {"asignatura": asignatura})
