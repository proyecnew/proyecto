from django.urls import path


from principal import views

urlpatterns = [
    
    path('', views.home, name="Home"),
    path('verificacion', views.verificacion, name="Verificacion"),
    path('deposito', views.deposito, name="Deposito"),
    
]