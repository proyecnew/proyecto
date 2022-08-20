from django.urls import path
from .views import VRegistro, logear, cerrar_sesion


urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('logear', logear, name="login"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
]