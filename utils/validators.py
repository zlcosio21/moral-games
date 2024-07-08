from django.contrib.auth.models import User
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


def len_errors(username, password):
    return len(username) < 8 or len(password) < 8


def different_passwords(password, password_confirm):
    return password != password_confirm


def verify_register_errors(user, username, email, password, password_confirm):
    return username_exist(user, username) or email_exist(user, email) or len_errors(username, password) or different_passwords(password, password_confirm)


def register_errors(request, username, email, password, password_confirm):
    user = request.user

    if username_exist(user, username):
        messages.error(request, "El nombre de usuario ya está en uso.", extra_tags="username_exist_error")

    if len(username) < 8:
        messages.error(request, "Debe contener mínimo 8 caracteres.", extra_tags="username_characters_error")

    if email_exist(user, email):
        messages.error(request, "El correo ingresado ya está en uso.", extra_tags="email_exist_error")

    if len(password) < 8:
        messages.error(request, "La contraseña debe contener mínimo 8 caracteres.", extra_tags="password_characters_error")

    if password != password_confirm:
        messages.error(request, "Las contraseñas deben ser iguales. Ingrese nuevamente.", extra_tags="equals_passwords_error")

    return verify_register_errors(user, username, email, password, password_confirm)


# Stock Videogames Validations
def stock_sold_out(videogame):
    return videogame.quantity < 1


def insufficient_stock(videogame, quantity):
    return videogame.quantity < int(quantity)


def stock_errors(request, videogame, quantity=1):

    if stock_sold_out(videogame):
        messages.error(request, f"Lo sentimos, actualmente esta entrega se encuentra agotada.", extra_tags="stock_sold_out")

    if insufficient_stock(videogame, quantity):
        messages.error(request, f"Solo se encuentran disponibles {videogame.cantidad} unidades del videojuego.", extra_tags="insufficient_stock")

    return stock_sold_out(videogame) or insufficient_stock(videogame, quantity)


def stock_errors_cart(request, cart):
    for item in cart:

        if stock_sold_out(item.videogame):
            Cart.delete_videogame(request, item.videogame)
            messages.error(request, f"Lastimosamente la entrega {item.videogame.name} se encuentra agotada, lo hemos eliminado de su carrito automaticamente.")
            return True

        if insufficient_stock(item.videogame, item.quantity):
            messages.error(request, f"Lastimosamente solo se encuentran disponibles {item.videogame.quantity} unidades de la entrega {item.videogame.nombre}.",)
            return True
