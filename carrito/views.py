from django.shortcuts import render
from carrito.models import Carrito
from tienda.models import HistorialCompra

# Create your views here.
def carrito(request, videojuego):
    carrito = Carrito.objects.get_or_create(usuario=request.user, videojuego=videojuego)
    carrito = Carrito.objects.filter(usuario=request.user)
    historial = HistorialCompra.objects.filter(usuario=request.user)

    return render(request, "carrito/prueba.html", {"carrito":carrito, "historial":historial})