from django.contrib import admin
from .models import Categoria, Desarrolladora, Plataforma, RequisitosSistema, Juego

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Desarrolladora)
class DesarrolladoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sitio_web')
    search_fields = ('nombre',)

@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(RequisitosSistema)
class RequisitosSistemaAdmin(admin.ModelAdmin):
    list_display = ('sistema_operativo', 'procesador', 'memoria_ram')
    search_fields = ('sistema_operativo', 'procesador')

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'desarrolladora', 'fecha_lanzamiento')
    list_filter = ('categorias', 'desarrolladora', 'plataformas')
    search_fields = ('titulo', 'descripcion')
    ordering = ('titulo',)
