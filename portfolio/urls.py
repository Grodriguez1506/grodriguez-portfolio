from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
    path('save/', views.save, name='save'),
    path('scrum-manager/', views.scrum_manager, name='scrum-manager'),
    path('password-generator/', views.password_generator, name='password-generator'),
    path('my-notebook/', views.my_notebook, name='my-notebook'),
]
