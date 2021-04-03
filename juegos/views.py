from django.shortcuts import render
from .models import Juego


def juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/juegos.html', {'juegos': juegos})