from django.db import models


class Semestre(models.Model):
    numero = models.IntegerField(verbose_name="Número de semestre")
    horas_totales = models.IntegerField(verbose_name="Horas totales del semestre")

    def __str__(self):
        return f"{self.numero}° Semestre"

    class Meta:
        db_table = "semestre"
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"
        ordering = ["numero"]


class Asignatura(models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.PROTECT, related_name="asignaturas")
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la asignatura")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código")
    creditos = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Créditos")

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        db_table = "asignatura"
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        ordering = ["semestre", "codigo"]
