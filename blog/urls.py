from django.urls import path
from . import views


# urls de la aplicacion de web

urlpatterns = [

    path('', views.blog, name='Blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name= 'categoria') # PARA PASARLE DESDE LA BASE DE DATOS
 
]
