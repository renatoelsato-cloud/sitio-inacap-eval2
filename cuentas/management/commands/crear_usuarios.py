from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

USUARIOS = [
    ("admin_demo", "Administrador", "admin_demo@example.com"),
    ("supervisor_demo", "Supervisor", "supervisor_demo@example.com"),
    ("administrativo_demo", "Administrativo", "administrativo_demo@example.com"),
]
CLAVE = "Inacap2026!"


class Command(BaseCommand):
    help = "Crea un usuario de prueba por cada grupo"

    def handle(self, *args, **options):
        for username, grupo, correo in USUARIOS:
            usuario, creado = User.objects.get_or_create(username=username, defaults={"email": correo})
            usuario.set_password(CLAVE)
            usuario.save()
            usuario.groups.set([Group.objects.get(name=grupo)])
            estado = "creado" if creado else "actualizado"
            self.stdout.write(self.style.SUCCESS(f"{username} ({grupo}): {estado}"))
