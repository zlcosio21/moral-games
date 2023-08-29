from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
import os
from dotenv import load_dotenv

# Email and password private
load_dotenv()
EMAIL = os.getenv("EMAIL")

# Create your views here.
def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("name")
        email = request.POST.get("email")
        mensaje = request.POST.get("message")

        envio_email = EmailMessage("Mensaje desde DjangoWebProject", "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {} ".format(nombre, email, mensaje), "",[EMAIL], reply_to=[email])

        try:
            envio_email.send() 
            return redirect("/contacto/?valido")
        except:
            return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html")