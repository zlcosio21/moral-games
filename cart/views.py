from utils.validators import stock_errors, stock_errors_cart
from utils.messages import success_message, error_message
from django.views.decorators.http import require_POST
from cart.models import Cart, ShoppingCartHistory
from django.shortcuts import render, redirect
from utils.emails import send_email_buy_cart
from inventory.models import Videogame


def cart(request):
    if not Cart.exists(request):
        error_message(request, "empty_cart")
        return redirect("inicio")

    cart = Cart.get_user_cart(request)
    total = Cart.get_total_user_cart(cart)

    return render(request, "cart/cart.html", {"cart": cart, "total": total})


def add_to_cart(request, id):
    videogame = Videogame.get(id=id)

    if Cart.videogame_in_cart(request, videogame):
        error_message(request, "videogame_already_in_cart")
        return redirect("tienda")

    if stock_errors(request, videogame):
        return redirect("tienda")

    Cart.add_videogame(request, videogame)

    return redirect("carrito")


@require_POST
def update_cart(request):
    cart = Cart.get_user_cart(request)
    Cart.update_cart(request, cart)

    success_message(request, "update_cart", "cart")

    return redirect("carrito")


def empty_cart(request):
    Cart.empty_cart(request)
    success_message(request, "empty_cart_succesfull", "cart")

    return redirect("inicio")


def delete_videogame_in_cart(request, id):
    videogame = Videogame.get(id=id)
    Cart.delete_videogame(request, videogame)

    if not Cart.exists(request):
        success_message(request, "empty_cart_succesfull", "cart")
        return redirect("inicio")

    return redirect("carrito")


@require_POST
def buy_cart(request):
    cart = Cart.get_user_cart(request)

    if stock_errors_cart(request, cart):
        return redirect("carrito")

    videogames = Cart.get_videogames_in_cart(cart)
    total = Cart.get_total_user_cart(cart)
    Videogame.update_stock_in_cart(cart)
    ShoppingCartHistory.save_order(request, videogames, total)

    country = request.POST.get("country")
    state = request.POST.get("state")
    postal_code = request.POST.get("postal_code")

    send_email_buy_cart(request, videogames, country, state, postal_code, total)
    success_message(request, "buy_cart", "cart")

    Cart.empty_cart(request)

    return redirect("inicio")
