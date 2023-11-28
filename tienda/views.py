from django.shortcuts import render, redirect
from inventario.models import Videojuego
from tienda.video import video
from django.db.models import Q, Value, IntegerField
from django.contrib import messages
from validators import stock_error, send_email_buy, save_order, validator_stock
from carrito.models import HistorialCompraCarrito
from tienda.models import HistorialCompra

# Create your views here.
def tienda(request):
    if request.method == "POST":
        busqueda = request.POST.get("busqueda")

        videojuegos = Videojuego.objects.filter(
            Q(nombre__icontains=busqueda) | 
            Q(plataforma__nombre__icontains=busqueda) | 
            Q(genero__nombre__icontains=busqueda)
        ).distinct()
        
        return render(request, "tienda/busqueda.html", {"videojuegos":videojuegos, "busqueda":busqueda})

    videojuego = Videojuego.objects.all()
    return render(request, "tienda/tienda.html", {"videojuegos":videojuego})

def compra(request, videojuego):
    videojuego = Videojuego.objects.get(nombre__iexact=videojuego)

    if request.method == "POST":
        cantidad = request.POST.get("quantity")

        if stock_error(request, cantidad, videojuego):
            return redirect("compra", videojuego=videojuego.nombre)

        validator_stock(videojuego, cantidad)
        send_email_buy(request, videojuego, cantidad)
        save_order(request, videojuego, cantidad)

        messages.success(request, f"Compra realizada exitosamente, factura enviada a su correo", extra_tags="buy_succesfull")
    
    nombre_videojuego = f"{videojuego.nombre} Official Trailer"
    video_url = video(nombre_videojuego)

    return render(request, "tienda/compra.html", {"video_url":video_url, "videojuego":videojuego, 'messages': messages.get_messages(request)})

def historial_compra(request):
    historial_compra = HistorialCompra.objects.filter(usuario=request.user).values("id", "videojuego", "created", "cantidad")
    
    historial_compra_carrito = HistorialCompraCarrito.objects.filter(usuario=request.user).values("id", "videojuego", "created")
    historial_compra_carrito = historial_compra_carrito.annotate(cantidad=Value(None, output_field=IntegerField()))

    historial_completo = historial_compra.union(historial_compra_carrito).order_by("created")

    return render(request, "tienda/historial_compra.html", {"historial_completo": historial_completo})