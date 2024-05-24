from MoralGamesWeb.base_models import Models
from django.db.models import Q
from django.db import models
import random


# Create your models here.
class Plataforma(Models):
    nombre = models.CharField(unique=True, max_length=50, null=False)

    def __str__(self):
        return f"Plataforma - {self.nombre}"


class Genero(Models):
    nombre = models.CharField(unique=True, max_length=50, null=False)

    def __str__(self):
        return f"Genero - {self.nombre}"


class Videojuego(Models):
    nombre = models.CharField(unique=True, max_length=50, null=False)
    imagen = models.ImageField(upload_to='tienda', null=False)
    precio = models.PositiveIntegerField(null=False)
    cantidad = models.PositiveIntegerField(null=False)
    genero = models.ManyToManyField(Genero)
    plataforma = models.ManyToManyField(Plataforma)
    informacion = models.CharField(max_length=300, null=True)

    @classmethod
    def random_videogames(cls):
        videojuego = list(cls.objects.all())
        random.shuffle(videojuego)

        return videojuego

    @classmethod
    def search(cls, busqueda):
        videojuegos = cls.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(plataforma__nombre__icontains=busqueda) |
            Q(genero__nombre__icontains=busqueda)
        ).distinct()

        return videojuegos

    def update_stock(self, cantidad):
        self.cantidad -= int(cantidad)
        self.save()

    def __str__(self):
        generos = ", ".join([genero.nombre for genero in self.genero.all()])
        plataformas = ", ".join([plataforma.nombre for plataforma in self.plataforma.all()])

        return f"{self.nombre} - Precio {self.precio} - Cantidad {self.cantidad} - Genero(s) {generos} - Plataforma(s) {plataformas}"
