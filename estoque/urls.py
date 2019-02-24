from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/', views.pdf, name='pdf'),
    path('filtrar/', views.filtrar, name='filtrar'),
    path('remover/<int:componente_id>/', views.remover, name='remover'),
]
