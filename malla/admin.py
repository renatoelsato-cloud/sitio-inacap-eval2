from django.contrib import admin
from .models import Semestre, Asignatura


class AsignaturaInline(admin.TabularInline):
    model = Asignatura
    extra = 1


class SemestreAdmin(admin.ModelAdmin):
    list_display = ("numero", "horas_totales")
    inlines = [AsignaturaInline]


class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "semestre", "creditos")
    list_filter = ("semestre",)
    search_fields = ("nombre", "codigo")


admin.site.register(Semestre, SemestreAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
