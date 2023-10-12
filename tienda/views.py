from django.shortcuts import render, redirect
from inventario.models import Genero, Plataforma, Videojuego
import os
from tienda.video import video
from django.db.models import Q

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
    nombre_videojuego = f"{videojuego.nombre} Official Trailer"
    video_url = video(nombre_videojuego)

    return render(request, "tienda/compra.html", {"video_url":video_url, "videojuego":videojuego})