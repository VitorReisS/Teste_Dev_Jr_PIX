from django.test import TestCase
from datetime import date
from decimal import Decimal
from .models import Agendamento

class AgendamentoTestCase(TestCase):

    def setUp(self):
        self.agendamento = Agendamento.objects.create(
            data_pagamento=date.today(),
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia="Ativa",
            agencia=1234,
            conta=567890,
            valor_pagamento=Decimal('150.75')
        )

    def test_agendamento_created(self):
        """Verifica se o objeto Agendamento foi criado corretamente."""
        self.assertEqual(Agendamento.objects.count(), 1)

    def test_valor_pagamento_conversion(self):
        """Verifica se o valor de pagamento foi salvo corretamente como inteiro."""
        agendamento = Agendamento.objects.create(
            data_pagamento='2024-09-13',
            permite_recorrencia=False,
            quantidade_recorrencia=1,
            intervalo_recorrencia=30,
            status_recorrencia="ativa",
            agencia=1234,
            conta=56789,
            valor_pagamento=Decimal('100.50')  # Definido como Decimal
        )
        # Verifique se foi salvo como inteiro no banco de dados
        self.assertEqual(agendamento.valor_pagamento, 10050)

    def test_atributos_agendamento(self):
        """Testa se os atributos do Agendamento foram salvos corretamente."""
        agendamento = Agendamento.objects.get(id=self.agendamento.id)
        self.assertTrue(agendamento.permite_recorrencia)
        self.assertEqual(agendamento.quantidade_recorrencia, 5)
        self.assertEqual(agendamento.intervalo_recorrencia, 30)
        self.assertEqual(agendamento.status_recorrencia, "Ativa")
        self.assertEqual(agendamento.agencia, 1234)
        self.assertEqual(agendamento.conta, 567890)

    def test_recorrencia_disabled(self):
        """Testa se o agendamento permite recorrência quando está desabilitado."""
        agendamento = Agendamento.objects.create(
            data_pagamento=date.today(),
            permite_recorrencia=False,
            quantidade_recorrencia=0,
            intervalo_recorrencia=0,
            status_recorrencia="Inativa",
            agencia=1234,
            conta=567890,
            valor_pagamento=Decimal('50.00')
        )
        self.assertFalse(agendamento.permite_recorrencia)
        self.assertEqual(agendamento.status_recorrencia, "Inativa")
