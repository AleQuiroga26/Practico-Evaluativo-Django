from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('juego/<int:id>/', views.detalle_juego, name='detalle_juego'),
    path('nuevo/', views.crear_juego, name='crear_juego'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),
]
