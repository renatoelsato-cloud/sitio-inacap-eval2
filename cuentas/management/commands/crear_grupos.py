from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

GRUPOS = {
    "Administrador": {
        "estudiante": ["add", "change", "delete", "view"],
        "asignatura": ["add", "change", "delete", "view"],
        "nota": ["add", "change", "delete", "view"],
        "user": ["add", "change", "delete", "view"],
        "group": ["view"],
    },
    "Supervisor": {
        "estudiante": ["add", "change", "view"],
        "asignatura": ["add", "change", "view"],
        "nota": ["add", "change", "view"],
    },
    "Administrativo": {
        "estudiante": ["view"],
        "asignatura": ["view"],
        "nota": ["add", "view"],
    },
}


class Command(BaseCommand):
    help = "Crea los grupos Administrador, Supervisor y Administrativo con sus permisos"

    def handle(self, *args, **options):
        for nombre, modelos in GRUPOS.items():
            grupo, _ = Group.objects.get_or_create(name=nombre)
            codenames = [f"{accion}_{modelo}" for modelo, acciones in modelos.items() for accion in acciones]
            permisos = Permission.objects.filter(codename__in=codenames)
            grupo.permissions.set(permisos)
            self.stdout.write(self.style.SUCCESS(f"{nombre}: {permisos.count()} permisos"))
