from django.shortcuts import render
from .models import Estacion


def estaciones(request):
    estaciones = Estacion.objects.all()
    return render(request, 'estaciones/estaciones.html', {'estaciones': estaciones})