from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
import os
from dotenv import load_dotenv
from validators import *
from django.contrib import messages
from django.contrib.auth import login

# Email and password private
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Create your views here.
def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        user = request.user
        exist = User.objects.filter(username=username).exclude(pk=user.pk).exists()

        username_exist(request, username)
        username_characters_error(request, username)
        characters_error(request, password)
        equals_error(request, password, password_confirm)

        if isvalid(request, username, password, password_confirm):

           user = User.objects.create_user(username=username, email=email, password=password)
           user.save()
           
           envio_email = EmailMessage("Mensaje desde MoralGames", "El usuario con nombre {}, ha registrado su cuenta, con correo {} \n\n ".format(username, email), "",[EMAIL], reply_to=[email])
           envio_email.send()

           login(request, user)

           return redirect("home")

    return render(request, "autenticacion/registro.html", {'messages': messages.get_messages(request)})