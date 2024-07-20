from django.urls import path
from gallery import views


urlpatterns = [

    path("", views.gallery, name="galeria"),
    path("ver_galeria_genero/<int:id>/", views.watch_gallery_genre, name="ver_galeria_genero"),

]
