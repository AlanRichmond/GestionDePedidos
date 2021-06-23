from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicio(request):
    servicios = Servicio.objects.all() # para que importe todos los servicios

    return render(request, 'servicios/servicios.html', {'servicios' : servicios})