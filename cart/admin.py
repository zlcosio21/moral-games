from cart.models import Cart, ShoppingCartHistory
from django.contrib import admin


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class ShoppingCartHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Cart, CartAdmin)
admin.site.register(ShoppingCartHistory, ShoppingCartHistoryAdmin)
