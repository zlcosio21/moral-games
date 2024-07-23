from django.urls import path, include
from django.contrib import admin


urlpatterns = [

    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("galeria/", include("gallery.urls")),
    path("blog/", include("blog.urls")),
    path("autenticacion/", include("authentication.urls")),
    path("tienda/", include("store.urls")),
    path("carrito/", include("cart.urls")),

]
