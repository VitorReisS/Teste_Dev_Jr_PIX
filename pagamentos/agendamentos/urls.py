from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/criar/', views.criar_agendamento, name='criar_agendamento'),  # POST
]