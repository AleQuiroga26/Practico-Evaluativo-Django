from django import forms
from .models import Juego

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'descripcion', 'precio', 'fecha_lanzamiento', 'portada', 'desarrolladora', 'plataformas', 'categorias', 'requisitos']
