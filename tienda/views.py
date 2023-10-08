from django.shortcuts import render
from inventario.models import Genero, Plataforma, Videojuego

# Create your views here.
def tienda(request):
    videojuego = Videojuego.objects.all()

    return render(request, "tienda/tienda.html", {"videojuegos":videojuego})