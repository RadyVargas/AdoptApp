from django.urls import path
from . import views
from .views import lista_contactos

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('animales/', views.animales, name='animales'),
    path("contacto/", views.lista_contactos, name="lista_contactos"),
    path('adoptar/<int:animal_id>/', views.adoptar_animal, name='adoptar_animal'),

]
