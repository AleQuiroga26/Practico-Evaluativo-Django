from django.shortcuts import render, redirect
from .forms import UsuarioPersonalizadoForm

def register(request):
    if request.method == 'POST':
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirige al login para que inicie sesión
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, 'registration/register.html', {'form': form})

