from django.urls import path
from malla import views as vista_malla
from malla import views_asignaturas as vista_asig

urlpatterns = [
    path('', vista_malla.inicio, name='inicio'),
    path('listado/', vista_malla.listado, name='listado'),
    path('asignaturas/', vista_asig.asignatura_listado, name='asignatura_listado'),
    path('asignaturas/nueva/', vista_asig.asignatura_crear, name='asignatura_crear'),
    path('asignaturas/<int:pk>/editar/', vista_asig.asignatura_editar, name='asignatura_editar'),
    path('asignaturas/<int:pk>/eliminar/', vista_asig.asignatura_eliminar, name='asignatura_eliminar'),
]

