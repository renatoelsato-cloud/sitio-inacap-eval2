from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms_notas import NotaForm
from .models import Nota


@login_required
@permission_required("egreso.view_nota", raise_exception=True)
def nota_listado(request):
    q = request.GET.get("q", "").strip()
    notas = Nota.objects.select_related("estudiante", "asignatura").all()
    if q:
        notas = notas.filter(Q(estudiante__nombre__icontains=q) | Q(asignatura__nombre__icontains=q) | Q(asignatura__codigo__icontains=q))
    return render(request, "egreso/nota_listado.html", {"notas": notas, "q": q})


@login_required
@permission_required("egreso.add_nota", raise_exception=True)
def nota_crear(request):
    form = NotaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            form.save()
        messages.success(request, "Nota registrada correctamente.")
        return redirect("nota_listado")
    return render(request, "egreso/nota_form.html", {"form": form})
