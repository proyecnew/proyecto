from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('verificacion/', include('verificacion.urls')),
    
    path('deposito/', include('deposito.urls')),
   
    path('', include('LoginApp.urls')),

    path('home/', include('principal.urls')),
    
    path('autenticacion/', include('autenticacion.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)