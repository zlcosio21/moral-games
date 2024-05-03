from carrito.models import HistorialCompraCarrito
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from inventario.models import Videojuego
from django.contrib import messages
from django.db.models import Q
from dotenv import load_dotenv
import os


# Environment Variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


# Authentication Validations
def register_errors(request, username, email, password, password_confirm):
    user = request.user
    username_exist = User.objects.filter(username=username).exclude(pk=user.pk).exists()
    email_exist = User.objects.filter(email=email).exclude(pk=user.pk).exists()

    if username_exist:
        messages.error(request, "El nombre de usuario ya está en uso.", extra_tags="username_exist_error")

    if len(username) < 8:
        messages.error(request, "Debe contener mínimo 8 caracteres", extra_tags="username_characters_error")

    if email_exist:
        messages.error(request, "El correo ingresado ya está en uso", extra_tags="email_exist_error")

    if len(password) < 8:
        messages.error(request, "La contraseña debe contener mínimo 8 caracteres", extra_tags="password_characters_error")

    if password != password_confirm:
        messages.error(request, "Las contraseñas deben ser iguales. Ingrese nuevamente", extra_tags="equals_passwords_error")

    return username_exist or email_exist or len(username) < 8 or len(password) < 8 or password != password_confirm


# Stock Videogames Validations
def stock_errors(request, videojuego, cantidad):
    insufficient_stock = videojuego.cantidad < int(cantidad)
    stock_sold_out = videojuego.cantidad < 1

    if stock_sold_out:
        messages.error(request, f"Lo sentimos, actualmente esta entrega se encuentra agotada", extra_tags="stock_sold_out")

    if insufficient_stock:
        messages.error(request, f"Solo se encuentran disponibles {videojuego.cantidad} unidades del videojuego", extra_tags="insufficient_stock")

    return insufficient_stock or stock_sold_out


# Send of Emails
def send_email_buy(request, videojuego, cantidad):
    total = (int(cantidad) * videojuego.precio)

    asunto = "Mensaje desde MoralGames, compra videojuego"
    cuerpo_mensaje = f"El cliente {request.user}, a realizado la compra de {cantidad} copias de {videojuego.nombre}. El total de la compra es de ${total}"
    destinatario = request.user.email

    email = EmailMessage(asunto, cuerpo_mensaje, "", [destinatario], reply_to=[EMAIL])
    email.send()


def send_email_buy_car(request, videojuegos, total):
    asunto = "Mensaje desde MoralGames, compra carrito"
    cuerpo_mensaje = f"El cliente {request.user}, ha realizado la compra de los siguientes videojuegos:\n\n"
    destinatario = request.user.email

    for videojuego in videojuegos:
        cuerpo_mensaje += f"{videojuego}\n"

    cuerpo_mensaje += f"\nEl total de la compra es de ${total}"

    email = EmailMessage(asunto, cuerpo_mensaje, "", [destinatario], reply_to=[EMAIL])
    email.send()


# Save Historial of buy
def save_order_car(request, videojuegos):
    videojuegos = ' '.join(videojuegos)
    guardar_pedido_carrito = HistorialCompraCarrito.objects.create(usuario=request.user, videojuego=videojuegos)
    guardar_pedido_carrito.save()


# Search
def search(busqueda):

    videojuegos = Videojuego.objects.filter(
        Q(nombre__icontains=busqueda) |
        Q(plataforma__nombre__icontains=busqueda) |
        Q(genero__nombre__icontains=busqueda)
    ).distinct()

    return videojuegos