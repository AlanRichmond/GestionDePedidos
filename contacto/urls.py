from django.urls import path
from . import views


# urls de la aplicacion de web

urlpatterns = [
    
    path('', views.contacto, name='Contacto'),
 
]