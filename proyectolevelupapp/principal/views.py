from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "principal/home.html")

def verificacion(request):
    return render(request, "principal/verificacion.html")


def deposito(request):
    return render(request, "principal/deposito.html")