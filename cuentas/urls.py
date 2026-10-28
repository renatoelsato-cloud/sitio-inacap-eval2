from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="cuentas/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("usuarios/", views.usuario_listado, name="usuario_listado"),
    path("usuarios/nuevo/", views.usuario_crear, name="usuario_crear"),
    path("usuarios/<int:pk>/editar/", views.usuario_editar, name="usuario_editar"),
    path("usuarios/<int:pk>/eliminar/", views.usuario_eliminar, name="usuario_eliminar"),
    path("recuperar/", auth_views.PasswordResetView.as_view(
        template_name="cuentas/recuperar_form.html",
        email_template_name="cuentas/recuperar_correo.txt",
        subject_template_name="cuentas/recuperar_asunto.txt",
    ), name="password_reset"),
    path("recuperar/enviado/", auth_views.PasswordResetDoneView.as_view(
        template_name="cuentas/recuperar_enviado.html"), name="password_reset_done"),
    path("restablecer/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="cuentas/restablecer_form.html"), name="password_reset_confirm"),
    path("restablecer/completo/", auth_views.PasswordResetCompleteView.as_view(
        template_name="cuentas/restablecer_completo.html"), name="password_reset_complete"),
]
