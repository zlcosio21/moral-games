from validators import send_email_contact
from django.shortcuts import render


# Create your views here.
def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("name")
        email = request.POST.get("email")
        mensaje = request.POST.get("message")

        send_email_contact(nombre, email, mensaje)

    return render(request, "contacto/contacto.html")