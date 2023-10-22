from django.shortcuts import render
from carrito.models import Carrito
from inventario.models import Videojuego
from django.contrib import messages

# Create your views here.
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)

    return render(request, "carrito/carrito.html", {"carrito":carrito})

def agregar_al_carrito(request, videojuego):
    videojuego = Videojuego.objects.get(nombre=videojuego)

    carrito = Carrito.objects.get_or_create(usuario=request.user, videojuego=videojuego)
    carrito = Carrito.objects.filter(usuario=request.user)

    return render(request, "carrito/carrito.html", {"carrito":carrito})

def vaciar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    carrito.delete()

    if not carrito:
        messages.success(request, "Se ha vaciado el carrito de compras", extra_tags="not_videogames_car")

    return render(request, "carrito/carrito.html", {"carrito":carrito})

def eliminar_del_carrito(request, videojuego):
    try:
        videojuego = Videojuego.objects.get(nombre=videojuego)
        eliminar_del_carrito = Carrito.objects.get(videojuego=videojuego)
        eliminar_del_carrito.delete()
    except Carrito.DoesNotExist:
        pass

    carrito = Carrito.objects.filter(usuario=request.user)

    return render(request, "carrito/carrito.html", {"carrito":carrito})