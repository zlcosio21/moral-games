from django.db import models
from django.contrib.auth.models import User
from validators import Models

# Create your models here - Creacion models
class Post(Models):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    contenido = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "post"
        plural_name = "posts"

    def __str__(self):
        return self.titulo