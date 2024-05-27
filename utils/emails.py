from django.core.mail import EmailMessage
from dotenv import load_dotenv
import os


# Environment Variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


# Send of Emails
def send_email_register(username, email):
    subject  = "Mensaje desde MoralGames"
    message_body  = f"El usuario con nombre {username}, ha registrado su cuenta, con correo {email} \n\n"
    recipient  = email

    user_email = EmailMessage(subject, message_body, "",[recipient], reply_to=[EMAIL])
    user_email.send()

    store_email = EmailMessage(subject, message_body, "",[EMAIL], reply_to=[recipient])
    store_email.send()


def send_email_buy(request, videogame, quantity):
    total = videogame.precio * int(quantity)

    subject = "Mensaje desde MoralGames, compra videojuego"
    message_body = f"El cliente {request.user}, a realizado la compra de {quantity} copias de {videogame.nombre}. El total de la compra es de ${total}"
    recipient = request.user.email

    email = EmailMessage(subject, message_body, "", [recipient], reply_to=[EMAIL])
    email.send()


def send_email_buy_car(request, videogames, total):
    subject = "Mensaje desde MoralGames, compra carrito"
    message_body = f"El cliente {request.user}, ha realizado la compra de los siguientes videojuegos:\n\n"
    recipient = request.user.email

    for videogame in videogames:
        message_body += f"{videogame}\n"

    message_body += f"\nEl total de la compra es de ${total}"

    email = EmailMessage(subject, message_body, "", [recipient], reply_to=[EMAIL])
    email.send()


def send_email_contact(name, email, message):
    subject = "Mensaje desde MoralGames"
    message_body = f"El usuario con nombre {name} con la direccion {email} escribe lo siguiente: \n\n {message}"

    email = EmailMessage(subject, message_body, "", [EMAIL] , reply_to=[email])
    email.send()
