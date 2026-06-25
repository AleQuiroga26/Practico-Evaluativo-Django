from django.shortcuts import render
from tienda.models import Juego

def bienvenida(request):
    juegos = Juego.objects.all()[:6] # Los juegos destacados arreglado sin precio
    return render(request, 'bienvenida/index.html', {'juegos': juegos})
