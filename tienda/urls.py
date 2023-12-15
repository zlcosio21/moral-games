from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.tienda, name="tienda"),
    path('compra/<str:videojuego>/', views.compra, name="compra"),
    path('historial_compra/', views.historial_compra, name="historial_compra")

]