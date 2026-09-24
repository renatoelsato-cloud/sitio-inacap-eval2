from django.contrib import admin
from .models import Estudiante, Nota, CampoLaboral, Competencia


class NotaInline(admin.TabularInline):
    model = Nota
    extra = 1


class CampoLaboralInline(admin.TabularInline):
    model = CampoLaboral
    extra = 1


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "rut", "correo", "anio_egreso")
    search_fields = ("nombre", "rut")
    inlines = [NotaInline, CampoLaboralInline]


class NotaAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "asignatura", "calificacion")
    list_filter = ("asignatura",)
    search_fields = ("estudiante__nombre",)


class CampoLaboralAdmin(admin.ModelAdmin):
    list_display = ("empresa", "cargo", "estudiante")
    search_fields = ("empresa", "cargo")


class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Nota, NotaAdmin)
admin.site.register(CampoLaboral, CampoLaboralAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
