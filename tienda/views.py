from django.shortcuts import render, redirect
from inventario.models import Videojuego
from tienda.video import video
from django.db.models import Q
from django.contrib import messages
from validators import stock_error, send_email_buy, save_order, validator_stock

# Create your views here.
def tienda(request):
    if request.method == "POST":
        busqueda = request.POST.get("busqueda")

        videojuegos = Videojuego.objects.filter(
            Q(nombre__icontains=busqueda) | 
            Q(plataforma__nombre__icontains=busqueda) | 
            Q(genero__nombre__icontains=busqueda)
        ).distinct()
        
        return render(request, "tienda/busqueda.html", {"videojuegos":videojuegos})

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