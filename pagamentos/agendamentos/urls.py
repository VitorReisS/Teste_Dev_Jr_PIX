from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
]