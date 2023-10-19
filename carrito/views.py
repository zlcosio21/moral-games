from django.shortcuts import render
from carrito.models import Carrito
from tienda.models import HistorialCompra
from inventario.models import Videojuego

# Create your views here.
def carrito(request, videojuego):
    videojuego = Videojuego.objects.get(nombre=videojuego)

    carrito = Carrito.objects.get_or_create(usuario=request.user, videojuego=videojuego)
    carrito = Carrito.objects.filter(usuario=request.user)

    return render(request, "carrito/carrito.html", {"carrito":carrito})