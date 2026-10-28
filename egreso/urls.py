from django.urls import path
from egreso import views as vista_egreso
from egreso import views_estudiantes as vista_est

urlpatterns = [
    path('', vista_egreso.perfil, name='perfil'),
    path('competencias/', vista_egreso.competencias, name='competencias'),
    path('notas/', vista_egreso.notas, name='notas'),
    path('estudiantes/', vista_est.estudiante_listado, name='estudiante_listado'),
    path('estudiantes/nuevo/', vista_est.estudiante_crear, name='estudiante_crear'),
    path('estudiantes/<int:pk>/editar/', vista_est.estudiante_editar, name='estudiante_editar'),
    path('estudiantes/<int:pk>/eliminar/', vista_est.estudiante_eliminar, name='estudiante_eliminar'),
]


