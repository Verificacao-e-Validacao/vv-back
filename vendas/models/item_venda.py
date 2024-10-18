from django.db import models
from produtos.models import Produto
from .venda import Venda
from django.core.exceptions import ValidationError
from django.db.models import Sum

class ItemVenda(models.Model):

    venda = models.ForeignKey(
        Venda, 
        related_name="itens", 
        on_delete=models.CASCADE,
    )
    
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE,
    )
    quantidade = models.PositiveIntegerField()
    
    valor_unitario = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

    def clean(self):
        """
            Verifica se existem produtos disponiveis no estoque
        """

        if self.quantidade > self.produto.movimentacoes_estoque.aggregate(total=Sum('quantidade'))['total']:
            raise ValidationError('Quantidade indisponivel no estoque.')

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f'Item Venda: {self.id} - Venda: {self.venda.id}'

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'vendas'
        verbose_name = 'Item Venda'
        verbose_name_plural = 'Itens de Vendas'
