from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Juego, Categoria
from .forms import JuegoForm

@login_required
def tienda(request):
    juegos = Juego.objects.all()
    categorias = Categoria.objects.all()
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    categoria_nombre = ''

    # Filtro por búsqueda
    if query:
        juegos = juegos.filter(titulo__icontains=query)

    # Filtro por categoría
    if categoria_id:
        categoria_id = int(categoria_id)
        juegos = juegos.filter(categorias__id=categoria_id)
        cat = Categoria.objects.filter(id=categoria_id).first()
        if cat:
            categoria_nombre = cat.nombre

    return render(request, 'tienda/index.html', {
        'juegos': juegos,
        'categorias': categorias,
        'query': query,
        'categoria_actual': categoria_id,
        'categoria_nombre': categoria_nombre,
    })

@login_required
def detalle_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    return render(request, 'tienda/detalle.html', {'juego': juego})

@login_required
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = JuegoForm()
    return render(request, 'tienda/crear_juego.html', {'form': form})

@login_required
def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('tienda')
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'tienda/editar_juego.html', {'form': form})

@login_required
def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        juego.delete()
        return redirect('tienda')
    return render(request, 'tienda/eliminar_juego.html', {'juego': juego})
