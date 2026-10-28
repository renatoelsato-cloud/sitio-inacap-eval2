from django import forms
from django.contrib.auth.models import Group, User


class UsuarioCrearForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"class": "form-control"}), min_length=8)
    grupo = forms.ModelChoiceField(label="Perfil", queryset=Group.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {"username": "Usuario", "first_name": "Nombre", "last_name": "Apellido", "email": "Correo"}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if not email:
            raise forms.ValidationError("El correo es obligatorio (se usa para recuperar la contraseña).")
        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un usuario con ese correo.")
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password"])
        if commit:
            usuario.save()
            usuario.groups.set([self.cleaned_data["grupo"]])
        return usuario


class UsuarioEditarForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(label="Perfil", queryset=Group.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    is_active = forms.BooleanField(label="Usuario activo", required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_active"]
        labels = {"first_name": "Nombre", "last_name": "Apellido", "email": "Correo"}
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            primero = self.instance.groups.first()
            if primero:
                self.fields["grupo"].initial = primero

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if not email:
            raise forms.ValidationError("El correo es obligatorio.")
        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un usuario con ese correo.")
        return email

    def save(self, commit=True):
        usuario = super().save(commit=commit)
        if commit:
            usuario.groups.set([self.cleaned_data["grupo"]])
        return usuario
