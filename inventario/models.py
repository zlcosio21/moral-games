from django.db import models
from django.core.validators import MinValueValidator,  MaxValueValidator

# Create your models here.
class Plataforma(models.Model):
    nombre = models.CharField(unique=True, max_length=50, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plataforma - {self.nombre}"

class Genero(models.Model):
    nombre = models.CharField(unique=True, max_length=50, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Genero - {self.nombre}"

class Videojuego(models.Model):
    nombre = models.CharField(unique=True, max_length=50, null=False)
    imagen = models.ImageField(upload_to='tienda', null=False)
    precio = models.PositiveIntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    cantidad = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    genero = models.ManyToManyField(Genero)
    plataforma = models.ManyToManyField(Plataforma)
    informacion = models.CharField(max_length=300, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        generos = ", ".join([genero.nombre for genero in self.genero.all()])
        plataformas = ", ".join([plataforma.nombre for plataforma in self.plataforma.all()])
        
        return f"{self.nombre} - Precio {self.precio} - Cantidad {self.cantidad} - Genero(s) {generos} - Plataforma(s) {plataformas}"
