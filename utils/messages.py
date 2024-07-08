from django.contrib import messages


SUCCESS_MESSAGES = {
    "buy_cart": "Compra realizada satisfactoriamente, revise su email para conocer mas a detalle.",
    "update_cart": "Se ha actualizado el carrito exitosamente.",
    "empty_cart_succesfull": "Se ha vaciado el carrito exitosamente.",
    "message_contact": "Se ha enviado el mensaje correctamente.",
}


ERROR_MESSAGES = {
    "logged_to_use_cart": "Debe iniciar sesión para poder usar el carrito.",
    "videogame_already_in_cart": "El videojuego ya se encuentra en el carrito de compras.",
    "empty_cart": "Carrito vacío, primero agregue un videojuego al carrito.",
    "account_not_exist": "La cuenta no existe, ingrese los datos nuevamente.",
    "platform_not_exist": "La plataforma no existe, fue redirigido a otra plataforma.",
}


def success_message(request, name_message, tag=""):
    return messages.success(
        request, SUCCESS_MESSAGES[name_message], extra_tags=tag if tag else ""
    )


def error_message(request, name_message, tag=""):
    return messages.success(
        request, ERROR_MESSAGES[name_message], extra_tags=tag if tag else ""
    )
