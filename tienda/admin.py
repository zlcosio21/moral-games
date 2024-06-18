from django.contrib import admin
from tienda.models import HistorialCompra, Video

# Register your models here.
class HistorialCompraAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(HistorialCompra, HistorialCompraAdmin)
admin.site.register(Video, VideoAdmin)