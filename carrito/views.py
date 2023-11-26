from django.shortcuts import render, redirect
from carrito.models import Carrito
from inventario.models import Videojuego
from django.contrib import messages
from validators import stock_error, save_order_car

# Create your views here.
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)

    return render(request, "carrito/carrito.html", {"carrito":carrito})

def agregar_al_carrito(request, videojuego):
    videojuego = Videojuego.objects.get(nombre=videojuego)
    en_carrito = Carrito.objects.filter(usuario=request.user, videojuego=videojuego)

    if request.method == "POST":
        cantidad = request.POST.get("quantity")

    if en_carrito:
        messages.error(request, "El videojuego ya se encuentra en el carrito de compras", extra_tags="videogame_in_car")
        return redirect("compra", videojuego=videojuego.nombre)

    if stock_error(request, cantidad, videojuego):
        return redirect("compra", videojuego=videojuego.nombre)
    
    carrito = Carrito.objects.get_or_create(usuario=request.user, videojuego=videojuego, cantidad=cantidad)

    return redirect("carrito")

def vaciar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    carrito.delete()

    return redirect("carrito")

def eliminar_del_carrito(request, videojuego):
    try:
        videojuego = Videojuego.objects.get(nombre=videojuego)
        eliminar_del_carrito = Carrito.objects.get(videojuego=videojuego)
        eliminar_del_carrito.delete()
    except Carrito.DoesNotExist:
        pass

    return redirect("carrito")

def comprar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    lista_videojuegos = []
    total = 0

    for item in carrito:
        total += item.videojuego.precio * item.cantidad

        videojuego = Videojuego.objects.get(nombre = item.videojuego.nombre)
        videojuego.cantidad -= item.cantidad
        videojuego.save()

        lista_videojuegos.append(str(f"{videojuego.nombre} - {item.cantidad} unidades,"))

    save_order_car(request, lista_videojuegos)
    
    messages.success(request, f"Compra realizada satisfactoriamente, el total de la compra es de ${total}, revise su email", extra_tags="buy_car_success")
    carrito.delete()

    return redirect("carrito")