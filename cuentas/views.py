from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    grupos = list(request.user.groups.values_list("name", flat=True))
    return render(request, "cuentas/dashboard.html", {"grupos": grupos})
