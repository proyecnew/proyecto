from email.mime import image
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from turtle import update
from venv import create
from django.db import models

class Persona(models.Model):
    usuario=models.CharField(max_length=50)
    foto=models.ImageField(upload_to="verificacion", null=True, blank=True)
    monto=models.FloatField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.usuario
    
class Deposito(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    foto=models.ImageField(upload_to="verificacion", null=True, blank=True)
    valor=models.FloatField()
    telefono=models.CharField(max_length=20)
    banco=models.CharField(max_length=20)
    cuenta=models.CharField(max_length=20)
    respuesta=models.BooleanField(blank=True, null=True)
    
    mensaje=models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
