from django.shortcuts import render

# Create your views here.
def autenticacion(request):

    return render(request, "autenticacion/registro.html")