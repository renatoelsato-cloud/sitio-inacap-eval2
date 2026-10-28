from datetime import date

from django import forms

from .models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre", "rut", "correo", "anio_egreso"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "rut": forms.TextInput(attrs={"class": "form-control", "placeholder": "12345678-9"}),
            "correo": forms.EmailInput(attrs={"class": "form-control"}),
            "anio_egreso": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_anio_egreso(self):
        anio = self.cleaned_data["anio_egreso"]
        if anio < 1990 or anio > date.today().year + 1:
            raise forms.ValidationError("Ingresa un año de egreso válido.")
        return anio
