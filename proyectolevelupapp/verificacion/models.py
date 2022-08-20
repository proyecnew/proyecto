from email.mime import image
from statistics import mode
from tkinter import CASCADE
from turtle import update
from venv import create
from django.db import models

class Usuario(models.Model):
    usuario=models.CharField(max_length=50)
    foto=models.ImageField(upload_to="verificacion", null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.usuario
    
class Verificacion(models.Model):
    persona = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    dpi=models.CharField(max_length=50)
    foto=models.ImageField(upload_to="verificacion", null=True, blank=True)
    pose1=models.ImageField(upload_to="verificacion", null=True, blank=True)
    pose2=models.ImageField(upload_to="verificacion", null=True, blank=True)
    selfie1=models.ImageField(upload_to="verificacion", null=True, blank=True)
    selfie2=models.ImageField(upload_to="verificacion", null=True, blank=True)
    respuesta=models.BooleanField(blank=True, null=True)
    documento=models.ImageField(upload_to="verificacion",null=True, blank=True)
    mensaje=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
