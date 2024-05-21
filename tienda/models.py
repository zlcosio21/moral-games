from django.contrib.auth.models import User
from MoralGamesWeb.base_models import Models
from youtubesearchpython import VideosSearch
from django.db import models


# Create your models here.
class HistorialCompra(Models):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField(null=False)

    @classmethod
    def save_order(cls, request, videojuego, cantidad):
        guardar_pedido = cls.objects.create(usuario=request.user, videojuego=videojuego.nombre, cantidad=cantidad)
        guardar_pedido.save()

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario} - {self.videojuego} - {self.cantidad} unidades - Realizado {self.created}"


class Video(Models):
    name = models.CharField(max_length=150, unique=True, null=False)
    url = models.CharField(max_length=300, unique=True, null=False)

    @classmethod
    def exist(cls, videogame):
        return cls.objects.filter(name=videogame).exists()

    @classmethod
    def found_url(cls, videogame):
        search = VideosSearch(videogame, limit=1)
        results = search.result()

        return results["result"][0]["link"].split("v=")[1]

    @classmethod
    def search(cls, videogame):
        if cls.exist(videogame):
            return cls.objects.get(name=videogame).url

        url = cls.found_url(videogame)
        cls.objects.create(name=videogame, url=url)

        return url

    def __str__(self):
        return f"Video {self.name} - Url {self.url}"
