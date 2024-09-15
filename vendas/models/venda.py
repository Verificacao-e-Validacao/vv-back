from django.db import models


class Venda(models.Model):

    vendedor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    valor_total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00
    )

    data_venda = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f'Venda {self.id} - {self.vendedor}'

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'vendas'
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
