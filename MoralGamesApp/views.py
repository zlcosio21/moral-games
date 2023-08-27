from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "MoralGamesApp/home.html")

def contacto(request):
    return render(request, "MoralGamesApp/contacto.html")


def blog(request):
    return render(request, "MoralGamesApp/blog.html")


def servicios(request):
    return render(request, "MoralGamesApp/servicios.html")


def tienda(request):
    return render(request, "MoralGamesApp/tienda.html")