from django.db import models
from malla.models import Asignatura


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre completo")
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    correo = models.EmailField(verbose_name="Correo electrónico")
    anio_egreso = models.IntegerField(verbose_name="Año de egreso")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "estudiante"
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["nombre"]


class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="notas")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT, related_name="notas")
    calificacion = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Calificación")

    def __str__(self):
        return f"{self.estudiante} - {self.asignatura} ({self.calificacion})"

    class Meta:
        db_table = "nota"
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ["estudiante", "asignatura"]


class CampoLaboral(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True, blank=True, related_name="campos_laborales")
    empresa = models.CharField(max_length=150, verbose_name="Empresa")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)

    def __str__(self):
        return f"{self.empresa} - {self.cargo}"

    class Meta:
        db_table = "campo_laboral"
        verbose_name = "Campo Laboral"
        verbose_name_plural = "Campos Laborales"
        ordering = ["empresa"]
