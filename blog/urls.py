from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from blog import views


urlpatterns = [

    path('', views.blog, name="blog"),
    path('ver_post/<int:id>/', views.watch_post, name="ver_post"),
    path('agregar_comentario_a_post/<int:id>/', views.add_comment_to_post, name="agregar_comentario_a_post"),
    path('agregar_comentario_a_videojuego/<int:id>/', views.add_comment_to_videogame, name="agregar_comentario_a_videojuego"),

]

urlpatterns += staticfiles_urlpatterns()