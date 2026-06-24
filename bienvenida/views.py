from django.shortcuts import render
from tienda.models import Juego

def bienvenida(request):
    juegos = Juego.objects.all()[:6] # Mostramos los primeros 6 como destacados
    return render(request, 'bienvenida/index.html', {'juegos': juegos})
