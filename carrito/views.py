from utils.validators import stock_errors, stock_errors_car
from carrito.models import Carrito, HistorialCompraCarrito
from django.shortcuts import render, redirect
from utils.emails import send_email_buy_car
from inventario.models import Videojuego
from django.contrib import messages


# Create your views here.
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)

    return render(request, "carrito/carrito.html", {"carrito":carrito})


def agregar_al_carrito(request, videojuego):
    videojuego = Videojuego.objects.get(nombre=videojuego)
    en_carrito = Carrito.objects.filter(usuario=request.user, videojuego=videojuego)

    if en_carrito:
        messages.error(request, "El videojuego ya se encuentra en el carrito de compras", extra_tags="videogame_in_car")
        return redirect("compra", videojuego=videojuego.nombre)

    if request.method == "POST":
        cantidad = request.POST.get("quantity")

    if stock_errors(request, videojuego, cantidad):
        return redirect("compra", videojuego=videojuego.nombre)

    Carrito.objects.get_or_create(usuario=request.user, videojuego=videojuego, cantidad=cantidad)

    return redirect("carrito")


def vaciar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    carrito.delete()

    return redirect("carrito")


def eliminar_del_carrito(request, videojuego):
    videojuego = Videojuego.objects.get(nombre=videojuego)

    carrito = Carrito.objects.get(usuario=request.user, videojuego=videojuego)
    carrito.delete()

    return redirect("carrito")


def comprar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)

    if stock_errors_car(request, carrito):
        return redirect("carrito")

    videojuegos = Carrito.videojuegos(carrito)
    total = Carrito.total_carrito(carrito)
    carrito.delete()

    HistorialCompraCarrito.save_order(request, videojuegos)

    send_email_buy_car(request, videojuegos, total)

    messages.success(request, f"Compra realizada satisfactoriamente, el total de la compra es de ${total}, revise su email", extra_tags="buy_car_success")

    return redirect("carrito")
