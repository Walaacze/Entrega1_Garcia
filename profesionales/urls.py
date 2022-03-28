from django.urls import path
from . import views

urlpatterns = [
    path('permanente/crear/', views.crear_permanente, name='crear_permanente'),
    path('permanentes/', views.lista_permanentes, name='lista_permanentes'),
    path('freelance/crear/', views.crear_freelance, name='crear_freelance'),
    path('freelances/', views.lista_freelances, name='lista_freelances'),
    path('administrativo/crear/', views.crear_administrativo, name='crear_administrativo'),
    path('administrativos/', views.lista_administrativos, name='lista_administrativos')
    
]
