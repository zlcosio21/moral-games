from django.db import models
from inventario.models import Videojuego
from django.contrib.auth.models import User

# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.CharField(max_length=75, unique=True)
    cantidad = models.PositiveSmallIntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Usuario {self.usuario} - Producto {self.videojuego} - {self.cantidad} unidades"