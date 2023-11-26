from django.db import models
from inventario.models import Videojuego
from django.contrib.auth.models import User
from MoralGamesWeb.base_models import Models

# Create your models here.
class Carrito(Models):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"Usuario {self.usuario} - Producto {self.videojuego.nombre} - {self.cantidad} unidades"
    
class HistorialCompraCarrito(Models):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.CharField(max_length=5000)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario} - {self.videojuego} - Realizado {self.created}"