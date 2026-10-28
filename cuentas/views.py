from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Avg, Q
from django.shortcuts import get_object_or_404, redirect, render

from egreso.models import Estudiante, Nota
from malla.models import Asignatura

from .forms import UsuarioCrearForm, UsuarioEditarForm


@login_required
def dashboard(request):
    user = request.user
    grupos = set(user.groups.values_list("name", flat=True))
    contexto = {
        "total_estudiantes": Estudiante.objects.count(),
        "total_asignaturas": Asignatura.objects.count(),
        "total_notas": Nota.objects.count(),
    }

    if user.is_superuser or "Administrador" in grupos:
        contexto["total_usuarios"] = User.objects.count()
        contexto["ultimas_notas"] = Nota.objects.select_related("estudiante", "asignatura").order_by("-id")[:5]
        return render(request, "cuentas/dashboard_admin.html", contexto)

    if "Supervisor" in grupos:
        contexto["promedio"] = Nota.objects.aggregate(p=Avg("calificacion"))["p"]
        contexto["ultimas_notas"] = Nota.objects.select_related("estudiante", "asignatura").order_by("-id")[:5]
        return render(request, "cuentas/dashboard_supervisor.html", contexto)

    return render(request, "cuentas/dashboard_administrativo.html", contexto)


@login_required
@permission_required("auth.view_user", raise_exception=True)
def usuario_listado(request):
    q = request.GET.get("q", "").strip()
    usuarios = User.objects.prefetch_related("groups").order_by("username")
    if q:
        usuarios = usuarios.filter(Q(username__icontains=q) | Q(email__icontains=q) | Q(first_name__icontains=q))
    return render(request, "cuentas/usuario_listado.html", {"usuarios": usuarios, "q": q})


@login_required
@permission_required("auth.add_user", raise_exception=True)
def usuario_crear(request):
    form = UsuarioCrearForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Usuario creado correctamente.")
        return redirect("usuario_listado")
    return render(request, "cuentas/usuario_form.html", {"form": form, "titulo": "Crear usuario"})


@login_required
@permission_required("auth.change_user", raise_exception=True)
def usuario_editar(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    form = UsuarioEditarForm(request.POST or None, instance=usuario)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Usuario modificado correctamente.")
        return redirect("usuario_listado")
    return render(request, "cuentas/usuario_form.html", {"form": form, "titulo": "Modificar usuario"})


@login_required
@permission_required("auth.delete_user", raise_exception=True)
def usuario_eliminar(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if usuario == request.user:
        messages.error(request, "No puedes eliminar tu propio usuario.")
        return redirect("usuario_listado")
    if request.method == "POST":
        usuario.delete()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect("usuario_listado")
    return render(request, "cuentas/usuario_confirmar_eliminar.html", {"usuario": usuario})
