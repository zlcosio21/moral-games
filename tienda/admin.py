from django.contrib import admin
from tienda.models import HistorialCompra

# Register your models here.
class HistorialCompraAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

admin.site.register(HistorialCompra, HistorialCompraAdmin)