from django.contrib.auth.models import User
from utils.messages import error_message
from django.contrib import messages
from cart.models import Cart


# Register user account
def create_user(user, username, email, password):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    return user


# Authentication Validations
def logged_in(request):
    return request.user.is_authenticated


def username_exist(user, username):
    return User.objects.filter(username=username).exclude(pk=user.pk).exists()


def email_exist(user, email):
    return User.objects.filter(email=email).exclude(pk=user.pk).exists()


def username_len_error(username):
    return len(username) < 8


def password_len_error(password):
    return len(password) < 8


def different_passwords(password, password_confirm):
    return password != password_confirm


def register_errors(request, username, email, password, password_confirm):
    user = request.user

    username_exists = username_exist(user, username)
    username_too_short = username_len_error(username)
    email_already_used = email_exist(user, email)
    password_too_short = password_len_error(password)
    passwords_do_not_match = different_passwords(password, password_confirm)
    
    if username_exists:
        error_message(request, "username_exist_error")

    if username_too_short:
        error_message(request, "username_characters_error")

    if email_already_used:
        error_message(request, "email_exist_error")

    if password_too_short:
        error_message(request, "password_characters_error")

    if passwords_do_not_match:
        error_message(request, "equals_passwords_error")

    errors = [
        username_exists,
        username_too_short,
        email_already_used,
        password_too_short,
        passwords_do_not_match
    ]

    return any(errors)


# Stock Videogames Validations
def stock_sold_out(videogame):
    return videogame.quantity < 1


def insufficient_stock(videogame, quantity):
    return videogame.quantity < int(quantity)


def stock_errors(request, videogame, quantity=1):
    stock_videogame_sold_out = stock_sold_out(videogame)

    if stock_videogame_sold_out:
        messages.error(request, "Lo sentimos, actualmente esta entrega se encuentra agotada.", extra_tags="stock_sold_out")

    return stock_videogame_sold_out


def stock_errors_cart(request, cart):
    for item in cart:
        videogame = item.videogame
        quantity = item.quantity

        if stock_sold_out(videogame):
            Cart.delete_videogame(request, videogame)
            messages.error(request, f"Lastimosamente la entrega {videogame.name} se encuentra agotada, lo hemos eliminado de su carrito automáticamente.")
            return True

        if insufficient_stock(videogame, quantity):
            messages.error(request, f"Lastimosamente solo se encuentran disponibles {videogame.quantity} unidades de la entrega {videogame.name}.") 
            return True

