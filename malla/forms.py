from django import forms

from .models import Asignatura


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ["semestre", "nombre", "codigo", "creditos"]
        widgets = {
            "semestre": forms.Select(attrs={"class": "form-select"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "codigo": forms.TextInput(attrs={"class": "form-control", "placeholder": "TI3041"}),
            "creditos": forms.NumberInput(attrs={"class": "form-control", "step": "0.5"}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_codigo(self):
        return self.cleaned_data["codigo"].strip().upper()

    def clean_creditos(self):
        creditos = self.cleaned_data["creditos"]
        if creditos <= 0 or creditos > 20:
            raise forms.ValidationError("Los créditos deben estar entre 0.5 y 20.")
        return creditos
