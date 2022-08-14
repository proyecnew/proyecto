from django.contrib import admin

# Register your models here.
from .models import Verificacion, Usuario

admin.site.register(Usuario)
admin.site.register(Verificacion)