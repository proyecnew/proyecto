from django.urls import path
from LoginApp import views

urlpatterns = [
    path('', views.home, name="Inicio"),
]
