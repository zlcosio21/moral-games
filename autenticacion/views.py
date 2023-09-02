from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
import os
from dotenv import load_dotenv

# Email and password private
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Create your views here.
def autenticacion(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password == password_confirm:

           user = User.objects.create_user(username=username, email=email, password=password)
           user.save()
           
           envio_email = EmailMessage("Mensaje desde MoralGames", "El usuario con nombre {}, ha registrado su cuenta, con correo {} \n\n ".format(username, email), "",[EMAIL], reply_to=[email])
           envio_email.send()

           return redirect("home")
        
        else:
            return redirect("/autenticacion/?novalido")

    return render(request, "autenticacion/registro.html")