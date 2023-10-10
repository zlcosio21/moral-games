from django.shortcuts import render
from inventario.models import Genero, Plataforma, Videojuego
import os
from tienda.video import video

# Create your views here.
def tienda(request):
    videojuego = Videojuego.objects.all()

    return render(request, "tienda/tienda.html", {"videojuegos":videojuego})

def compra(request, videojuego):
    videojuego = Videojuego.objects.get(nombre__iexact=videojuego)
    nombre_videojuego = f"{videojuego.nombre} Official Trailer"
    video_url = video(nombre_videojuego)

    return render(request, "tienda/compra.html", {"video_url":video_url, "videojuego":videojuego})