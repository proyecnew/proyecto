from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Persona

def deposito(request):
    usuario_lista = Persona.objects.all()
    return render(request, "deposito/deposito.html", {
        "usuario_lista": usuario_lista
    })

def usuario(request, persona_id ):
    persona = get_object_or_404(Persona, pk=persona_id)
    return render(request, "deposito/usuario.html", {
        "persona": persona
    }) 

def resultado(request, persona_id):
    return HttpResponse(f"Su mensaje fue venviado con exito" )

    
