from django.urls import path, include
from carrito import views
from django.conf import settings

urlpatterns = [

    path('', views.carrito, name="carrito"),
    path('agregar_al_carrito/<str:videojuego>/', views.agregar_al_carrito, name="agregar_al_carrito"),
    path('vaciar_carrito/', views.vaciar_carrito, name="vaciar_carrito"),
        
]