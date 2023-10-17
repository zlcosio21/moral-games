from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,  MaxValueValidator
from inventario.models import Videojuego

# Create your models here.
class HistorialCompra(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(1000)])

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario} - {self.videojuego} - {self.cantidad} unidades - Realizado {self.created}"
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Usuario {self.usuario} - Producto {self.videojuego.nombre} - {self.cantidad} unidades"