from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from django.shortcuts import render

from egreso.models import Estudiante, Nota
from malla.models import Asignatura


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
