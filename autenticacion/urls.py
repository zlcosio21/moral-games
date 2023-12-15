from django.urls import path
from autenticacion import views

urlpatterns = [

    path('', views.registro, name="registro"),
    path('inicio_sesion/', views.inicio_sesion, name="inicio_sesion"),
    path('cerrar_sesion/', views.cerrar_sesion, name="cerrar_sesion")

]