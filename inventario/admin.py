from django.contrib import admin
from .models import Plataforma, Genero, Videojuego

# Register your models here.
class PlataformaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class GeneroAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class VideojuegoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Videojuego, VideojuegoAdmin)