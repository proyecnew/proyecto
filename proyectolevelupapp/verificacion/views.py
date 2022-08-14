from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse

from .models import Usuario

def verificacion(request):
    usuario_lista = Usuario.objects.all()
    return render(request, "verificacion/verificacion.html", {
        "usuario_lista": usuario_lista
    })

def usuario(request, persona_id ):
    persona = get_object_or_404(Usuario, pk=persona_id)
    return render(request, "verificacion/usuario.html", {
        "persona": persona
    })
    

    
    