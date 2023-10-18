from django.contrib import admin
from carrito.models import Carrito

# Register your models here.
class CarritoAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

admin.site.register(Carrito, CarritoAdmin)