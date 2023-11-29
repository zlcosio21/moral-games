from django.contrib import messages
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv
from django.core.mail import EmailMessage
from tienda.models import HistorialCompra
from carrito.models import HistorialCompraCarrito

load_dotenv()
EMAIL = os.getenv("EMAIL")
 
def username_characters_error(request, *username):
    for user in username:
        if len(user) < 8:
           return messages.error(request, "Debe contener minimo 8 caracteres", extra_tags="username_characters_error")

def characters_error(request, *args):
    for var in args:
        if len(var) < 8:
            return messages.error(request, "Debe contener minimo 8 caracteres", extra_tags="characters_error")

def username_exist(request, new_username):
    user = request.user
    exist = User.objects.filter(username=new_username).exclude(pk=user.pk).exists()

    if exist:
        return messages.error(request, "El nuevo nombre de usuario ya está en uso.", extra_tags="username_exist_error")

def password_invalid(request, password_actual):
    user = request.user

    password_valida = user.check_password(password_actual)
    if not password_valida:
        return messages.error(request, "La contraseña actual es incorrecta, ingrese nuevamente", extra_tags="password_invalid")
    
def equals_error(request, password, password_confirm):

    if password != password_confirm:
        return messages.error(request, "Las contraseñas deben ser iguales. Ingrese nuevamente", extra_tags="equals_error")
    
def isvalid(request, username, password, password_confirm):
    user = request.user
    exist = User.objects.filter(username=username).exclude(pk=user.pk).exists()

    if len(username) >= 8 and (len(password) >= 8 and len(password_confirm) >= 8) and password == password_confirm and not exist:
        return True
    else:
        return False
    
def validator_stock(videojuego, cantidad):
    if videojuego.cantidad >= int(cantidad):
        videojuego.cantidad -= int(cantidad)
        videojuego.save()

def stock_error(request, cantidad, videojuego):
    if videojuego.cantidad < int(cantidad) or videojuego.cantidad < 0:
        messages.error(request, f"Solo se encuentran disponibles {videojuego.cantidad} unidades del videojuego", extra_tags="stock_error")
        return True

def send_email_buy(request, videojuego, cantidad):
    total = (int(cantidad) * videojuego.precio)
    
    email = EmailMessage("Mensaje desde MoralGames", f"El cliente {request.user}, a realizado la compra de {cantidad} copias de {videojuego.nombre}. El total de la compra es de ${total}", "", [EMAIL], reply_to=[request.user.email])
    email.send()

def save_order(request, videojuego, cantidad):
    guardar_pedido = HistorialCompra.objects.create(usuario=request.user, videojuego=videojuego.nombre, cantidad=cantidad)
    guardar_pedido.save()

def save_order_car(request, videojuegos):
    videojuegos = ' '.join(videojuegos)
    guardar_pedido_carrito = HistorialCompraCarrito.objects.create(usuario=request.user, videojuego=videojuegos)
    guardar_pedido_carrito.save()

def send_email_buy_car(request, lista_videojuegos, total):
    cuerpo_correo = f"El cliente {request.user}, a realizado la compra de los siguientes videojuegos:\n\n"

    for videojuego in lista_videojuegos:
        cuerpo_correo += f"{videojuego}\n"

    cuerpo_correo += f"\n El total de la compra es de ${total}"

    email = EmailMessage("Mensaje desde MoralGames", cuerpo_correo, "", [EMAIL], reply_to=[request.user.email])
    email.send()