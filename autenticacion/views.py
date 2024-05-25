from utils.validators import register_user, register_errors
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from utils.emails import send_email_register
from django.contrib import messages


# Create your views here.
def registro(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if register_errors(request, username, email, password, password_confirm):
            return redirect("registro")

        user = register_user(user, username, email, password)

        send_email_register(username, email)

        login(request, user)

        return redirect("home")

    return render(request, "autenticacion/registro.html")


def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user == None:
            messages.error(request, "La cuenta no existe, ingrese los datos nuevamente", extra_tags="account_not_exist")
            return redirect("inicio_sesion")

        login(request, user)

        return redirect("home")

    return render(request, "autenticacion/inicio_sesion.html")


def cerrar_sesion(request):
    logout(request)

    return redirect("home")
