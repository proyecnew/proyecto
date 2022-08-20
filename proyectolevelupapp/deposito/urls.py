from lib2to3.pygram import pattern_symbols
from django.urls import path
from .models import Persona
from deposito import views


app_name = "abne"
urlpatterns = [
    
    path("", views.deposito, name="deposito"),
    path("<int:persona_id>/", views.usuario, name="usuario"),
    path("<int:persona_id>/resultado", views.resultado, name="resultado")
    
]
