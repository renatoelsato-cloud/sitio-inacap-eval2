from django.urls import path
from malla import views as vista_malla

urlpatterns = [
    path('', vista_malla.inicio, name='inicio'),
    path('listado/', vista_malla.listado, name='listado'),
]