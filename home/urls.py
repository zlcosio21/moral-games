from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from home import views


urlpatterns = [

    path("", views.home, name="inicio"),
    path("contacto/", views.contact, name="contacto"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
