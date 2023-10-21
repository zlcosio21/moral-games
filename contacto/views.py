from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from validators import EMAIL

# Create your views here.
def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("name")
        email = request.POST.get("email")
        mensaje = request.POST.get("message")

        envio_email = EmailMessage("Mensaje desde DjangoWebProject", "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {} ".format(nombre, email, mensaje), "",[EMAIL], reply_to=[email])
        envio_email.send() 

    return render(request, "contacto/contacto.html")