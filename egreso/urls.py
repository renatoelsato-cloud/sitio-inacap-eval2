from django.urls import path
from egreso import views as vista_egreso

urlpatterns = [
    path('', vista_egreso.perfil, name='perfil'),
    path('competencias/', vista_egreso.competencias, name='competencias'),
]