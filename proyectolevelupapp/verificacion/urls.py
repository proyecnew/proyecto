from lib2to3.pygram import pattern_symbols
from django.urls import path
from .models import Usuario
from verificacion import views


app_name = "abner"
urlpatterns = [
    
    path("", views.verificacion, name="verificacion"),
    path("<int:persona_id>/", views.usuario, name="usuario"),
    path("<int:persona_id>/resultado", views.resultado, name="resultado")
    
]
