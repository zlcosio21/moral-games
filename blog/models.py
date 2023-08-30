from django.db import models
from django.contrib.auth.models import User

# Create your models here - Creacion models
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    contenido = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name = "post"
        plural_name = "posts"

    def __str__(self):
        return self.titulo