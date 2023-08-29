from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from contacto import views

urlpatterns = [

    path('', views.contacto, name="contacto"),
        
]

urlpatterns += staticfiles_urlpatterns()