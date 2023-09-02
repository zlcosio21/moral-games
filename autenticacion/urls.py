from django.urls import path
from autenticacion import views

urlpatterns = [

    path('', views.autenticacion, name="autenticacion"),
        
]