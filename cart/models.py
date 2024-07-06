from moral_games.base_models import Models
from django.contrib.auth.models import User
from inventory.models import Videogame
from django.db import models


# Create your models here.
class Cart(Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def item_total(self):
        return self.videogame.price * self.quantity

    @classmethod
    def add_videogame(cls, request, videogame, quantity=1):
        return cls.objects.create(
            user=request.user, videogame=videogame, quantity=quantity
        )

    @classmethod
    def get_user_cart(cls, request):
        return cls.objects.filter(user=request.user)

    @classmethod
    def get_videogames_cart(cls, request, limit=0):
        if not cls.exists(request):
            return Videogame.get_random_videogames(2)

        if limit > 0:
            return cls.objects.filter(user=request.user).order_by("?")[:limit]

        return cls.objects.all().order_by("?")[:2]

    @staticmethod
    def get_total_user_cart(cart):
        return sum(item.videogame.price * item.quantity for item in cart)

    @staticmethod
    def get_videogames_in_cart(cart):
        return [
            f"{item.videogame.name} - {item.quantity} unidades - ${item.item_total()}."
            for item in cart
        ]

    @classmethod
    def delete_videogame(cls, request, videogame):
        cls.objects.get(user=request.user, videogame=videogame).delete()

    @classmethod
    def update_cart(cls, request, cart):
        for item in range(1, len(cart) + 1):
            id = request.POST.get(f"id_{item}")
            quantity = request.POST.get(f"quantity_{item}")

            carrito = cls.objects.get(id=id)
            carrito.quantity = quantity
            carrito.save()

    @classmethod
    def videogame_in_cart(cls, request, videogame):
        return cls.objects.filter(user=request.user, videogame=videogame).exists()

    @classmethod
    def empty_cart(cls, request):
        return cls.get_user_cart(request).delete()

    @classmethod
    def exists(cls, request):
        return cls.objects.filter(user=request.user).exists()

    def __str__(self):
        return f"Usuario {self.user} - Producto {self.videogame.name} - {self.quantity} unidades"
