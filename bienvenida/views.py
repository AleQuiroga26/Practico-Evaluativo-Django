from django.shortcuts import render
from tienda.models import Juego

def bienvenida(request):
    juegos = Juego.objects.all()[:5] # Los juegos destacados arreglado sin precio
    return render(request, 'bienvenida/index.html', {'juegos': juegos})
