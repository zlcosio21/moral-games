from django.shortcuts import render, redirect
from inventario.models import Genero, Plataforma, Videojuego
import os
from tienda.video import video
from django.db.models import Q
from dotenv import load_dotenv
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages

# Email and password private
load_dotenv()
EMAIL = os.getenv("EMAIL")

# Create your views here.
def tienda(request):
    if request.method == "POST":
        busqueda = request.POST.get("busqueda")
        
        videojuegos = Videojuego.objects.filter(
            Q(nombre__icontains=busqueda) | 
            Q(plataforma__nombre__icontains=busqueda) | 
            Q(genero__nombre__icontains=busqueda)
        ).distinct()
      
        if busqueda == " ":
            return redirect("tienda")
        
        return render(request, "tienda/busqueda.html", {"videojuegos":videojuegos})

    videojuego = Videojuego.objects.all()
    return render(request, "tienda/tienda.html", {"videojuegos":videojuego})

def compra(request, videojuego):
    videojuego = Videojuego.objects.get(nombre__iexact=videojuego)

    if request.method == "POST":
        cantidad = request.POST.get("quantity")

        if int(cantidad) > videojuego.cantidad:
            messages.error(request, f"Solo se encuentran disponibles {videojuego.cantidad} unidades del videojuego", extra_tags="stock_error")
        else:
            total = (int(cantidad) * videojuego.precio)
    
            envio_email = EmailMessage("Mensaje desde MoralGames", f"El cliente {request.user}, a realizado la compra de {cantidad} copias de {videojuego.nombre}. El total de la compra es de ${total}", "", [EMAIL], reply_to=[request.user.email])
            envio_email.send()

            messages.success(request, f"Compra realizada exitosamente, factura enviada a su correo", extra_tags="buy_succesfull")
    
    nombre_videojuego = f"{videojuego.nombre} Official Trailer"
    video_url = video(nombre_videojuego)

    return render(request, "tienda/compra.html", {"video_url":video_url, "videojuego":videojuego, 'messages': messages.get_messages(request)})