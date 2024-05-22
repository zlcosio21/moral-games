from django.shortcuts import render, redirect
from tienda.models import HistorialCompra
from utils.validators import stock_errors
from inventario.models import Videojuego
from utils.emails import send_email_buy
from utils.purchase_history import *
from django.contrib import messages
from tienda.models import Video


# Create your views here.
def tienda(request):
    videojuegos_random = Videojuego.random_videogames()

    if request.method == "POST":
        busqueda = request.POST.get("busqueda")
        videojuegos = Videojuego.search(busqueda)

        return render(request, "tienda/busqueda.html", {"videojuegos":videojuegos, "busqueda":busqueda})

    return render(request, "tienda/tienda.html", {"videojuegos":videojuegos_random})


def compra(request, videojuego):
    videojuego = Videojuego.objects.get(nombre__iexact=videojuego)
    video_url = Video.search(f"{videojuego.nombre} Videogame Official Trailer")

    if request.method == "POST":
        cantidad = request.POST.get("quantity")

        if stock_errors(request, videojuego, cantidad):
            return redirect("compra", videojuego=videojuego.nombre)

        videojuego.update_stock(cantidad)

        HistorialCompra.save_order(request, videojuego, cantidad)

        send_email_buy(request, videojuego, cantidad)

        messages.success(request, f"Compra realizada exitosamente, factura enviada a su correo", extra_tags="buy_succesfull")

    return render(request, "tienda/compra.html", {"video_url":video_url, "videojuego":videojuego})


def historial_compra(request):
    historial_compra = obtain_purchase_history(request.user)
    historial_carrito = obtain_car_history(request.user)
    historial_completo = obtain_complete_history(historial_compra, historial_carrito)

    return render(request, "tienda/historial_compra.html", {"historial_completo": historial_completo})
