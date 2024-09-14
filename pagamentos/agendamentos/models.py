from django.db import models

class Agendamento(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField()
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=100)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField()  # Armazena o valor como inteiro

    def save(self, *args, **kwargs):
        # Converte o valor do pagamento de decimal para inteiro antes de salvar
        if isinstance(self.valor_pagamento, float):
            self.valor_pagamento = int(self.valor_pagamento * 100)  # Exemplo de conversão para centavos
        super().save(*args, **kwargs)
