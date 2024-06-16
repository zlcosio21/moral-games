from MoralGamesWeb.base_models import Models
from django.contrib.auth.models import User
from inventario.models import Videojuego
from django.db import models


# Create your models here.
class Carrito(Models):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=1)

    @staticmethod
    def total_carrito(items_carrito):
        total = 0

        for item in items_carrito:
            total += item.videojuego.precio * item.cantidad
            videojuego = Videojuego.objects.get(nombre=item.videojuego.nombre)
            videojuego.cantidad -= item.cantidad
            videojuego.save()

        return total

    @staticmethod
    def videojuegos(items_carrito):
        videojuegos = []

        for item in items_carrito:
            videojuegos.append(str(f"{item.videojuego.nombre} - {item.cantidad} unidades,"))

        return videojuegos

    @staticmethod
    def eliminar_videojuego(request, videojuego):
        videojuego = Carrito.objects.get(usuario=request.user, videojuego=videojuego)
        videojuego.delete()

    def __str__(self):
        return f"Usuario {self.usuario} - Producto {self.videojuego.nombre} - {self.cantidad} unidades"


class HistorialCompraCarrito(Models):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.CharField(max_length=5000)

    @classmethod
    def save_order(cls, request, videojuegos):
        videojuegos = ' '.join(videojuegos)

        guardar_pedido_carrito = cls.objects.create(usuario=request.user, videojuego=videojuegos)
        guardar_pedido_carrito.save()

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario} - {self.videojuego} - Realizado {self.created}"