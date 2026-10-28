from decimal import Decimal

from django import forms

from .models import Nota


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["estudiante", "asignatura", "calificacion"]
        widgets = {
            "estudiante": forms.Select(attrs={"class": "form-select"}),
            "asignatura": forms.Select(attrs={"class": "form-select"}),
            "calificacion": forms.NumberInput(attrs={"class": "form-control", "step": "0.1"}),
        }

    def clean_calificacion(self):
        nota = self.cleaned_data["calificacion"]
        if nota < Decimal("1.0") or nota > Decimal("7.0"):
            raise forms.ValidationError("La calificación debe estar entre 1.0 y 7.0.")
        return nota

    def clean(self):
        datos = super().clean()
        estudiante = datos.get("estudiante")
        asignatura = datos.get("asignatura")
        if estudiante and asignatura:
            if Nota.objects.filter(estudiante=estudiante, asignatura=asignatura).exists():
                raise forms.ValidationError("Este estudiante ya tiene una nota en esa asignatura.")
        return datos
