from django.db import models
from decimal import Decimal

class Agendamento(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField()
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=50)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField()  # Armazenado como inteiro

    def save(self, *args, **kwargs):
        # Converter valor_pagamento de Decimal para inteiro antes de salvar
        if isinstance(self.valor_pagamento, Decimal):
            self.valor_pagamento = int(self.valor_pagamento * 100)
        super().save(*args, **kwargs)
