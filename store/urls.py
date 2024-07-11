from django.urls import path
from store import views

urlpatterns = [

    path('', views.store, name="tienda"),
    path('ver_videojuego/<int:id>/', views.watch_videogame, name="ver_videojuego"),
    path('historial_compra/', views.purchase_history, name="historial_compra"),
    path('probar_suerte/', views.try_luck, name="probar_suerte"),
    path('genero_videojuego/', views.watch_genre_videogames, name="genero_videojuego"),
    path('ver_genero_videojuego/<str:genre>/', views.watch_genre_videogames, name="ver_genero_videojuego"),
    path('plataforma_videojuego/', views.watch_platform_videogames, name="plataforma_videojuego"),
    path('ver_plataforma_videojuego/<str:platform>/', views.watch_platform_videogames, name="ver_plataforma_videojuego"),
    path('buscar/', views.search, name="buscar"),
    path('buscar_por_precio/', views.search_by_price, name="buscar_por_precio")

]