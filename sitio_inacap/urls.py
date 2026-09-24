from django.contrib import admin
from django.urls import path, include
from malla.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='home'),
    path('malla/', include('malla.urls')),
    path('egreso/', include('egreso.urls')),
]