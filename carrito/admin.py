from django.contrib import admin
from carrito.models import Carrito, HistorialCompraCarrito

# Register your models here.
class CarritoAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

class HistorialCompraCarritoAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

admin.site.register(Carrito, CarritoAdmin)
admin.site.register(HistorialCompraCarrito, HistorialCompraCarritoAdmin)