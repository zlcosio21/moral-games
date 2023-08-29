from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from MoralGamesApp import views

urlpatterns = [

    path('', views.home, name="home"),
    path('contacto/', include('contacto.urls')),
    path('blog/', views.blog, name="blog"),
    path('servicios/', views.blog, name="servicios"),
    path('tienda/', views.tienda, name="tienda"),
        
]

urlpatterns += staticfiles_urlpatterns()