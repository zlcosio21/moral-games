from django.urls import path
from cart import views

urlpatterns = [

    path('', views.cart, name="carrito"),
    path('agregar_al_carrito/<int:id>/', views.add_to_cart, name="agregar_al_carrito"),
    path('actualizar_carrito/', views.update_cart, name="actualizar_carrito"),
    path('vaciar_carrito/', views.empty_cart, name="vaciar_carrito"),
    path('eliminar_del_carrito/<int:id>/', views.delete_videogame_in_cart, name="eliminar_del_carrito"),
    path('comprar_carrito', views.buy_cart, name="comprar_carrito")

]