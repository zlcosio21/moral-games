from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from MoralGamesApp import views

urlpatterns = [

    path('', views.home, name="home"),
    path('servicios/', views.servicios, name="servicios"),
    path('tienda/', views.tienda, name="tienda"),
        
]

urlpatterns += staticfiles_urlpatterns()