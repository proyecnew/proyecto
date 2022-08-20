from django.contrib import admin

# Register your models here.
from .models import Deposito, Persona

admin.site.register(Persona)
admin.site.register(Deposito)