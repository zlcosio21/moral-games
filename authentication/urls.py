from django.urls import path
from authentication import views

urlpatterns = [

    path('', views.register_user, name="registro"),
    path('inicio_sesion/', views.login_user, name="inicio_sesion"),
    path('cerrar_sesion/', views.log_out_user, name="cerrar_sesion")

]