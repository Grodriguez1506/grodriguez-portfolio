from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyecto/<str:url>/', views.proyecto, name='proyecto'),
    path('contacto/', views.contacto, name='contacto'),
    path('save/', views.save, name='save'),
]
