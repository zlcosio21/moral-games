from django.db import models
from django.contrib.auth.models import User
from MoralGamesWeb.base_models import Models

# Create your models here.
class HistorialCompra(Models):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario} - {self.videojuego} - {self.cantidad} unidades - Realizado {self.created}"