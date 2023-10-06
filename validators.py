from django.contrib import messages
from django.contrib.auth.models import User
 
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