from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar, name='inicio'),  # Ruta para la página de inicio
    path('buscar/', views.buscar, name='buscar'),  # Ruta para la búsqueda
]

