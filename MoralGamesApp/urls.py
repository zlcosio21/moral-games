from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from MoralGamesApp import views

urlpatterns = [

    path('', views.home, name="home"),
    path('contacto/', views.contacto, name="contacto"),
    path('blog/', views.blog, name="blog"),
    path('servicios/', views.blog, name="servicios"),
    path('tienda/', views.tienda, name="tienda"),
        
]

urlpatterns += staticfiles_urlpatterns()