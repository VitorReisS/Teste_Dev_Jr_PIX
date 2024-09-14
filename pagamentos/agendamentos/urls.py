from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/criar/', views.criar_agendamento, name='criar_agendamento'),  # POST
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),  # GET
    path('agendamentos/<int:id>/', views.consultar_agendamento, name='consultar_agendamento'),  # GET
    path('agendamentos/<int:id>/deletar/', views.deletar_agendamento, name='deletar_agendamento'),  # DELETE
    path('agendamentos/<int:id>/atualizar/', views.atualizar_agendamento, name='atualizar_agendamento'), # PATCH
]