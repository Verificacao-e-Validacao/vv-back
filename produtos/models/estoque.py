from django.db import models
from .produto import Produto
from django.core.exceptions import ValidationError

class Estoque(models.Model):
    """
        Realiza a movimentação de estoque para um produto.
    """

    produto = models.ForeignKey(
        Produto, 
        on_delete=models.CASCADE, 
        related_name='movimentacoes_estoque',
        verbose_name="Produto"
    )
    
    data_movimentacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data da Movimentação"
    )

    peso = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Peso do produto em quilogramas",
        blank=True,
        null=True,
    )

    valor_compra = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Valor de compra do produto"
    )

    quantidade = models.IntegerField(
        help_text="Quantidade disponível em estoque"
    )

    vencimento = models.DateField(
        help_text="Data de vencimento do produto",
        blank=True,
        null=True,
    )

    def clean(self):
        """
            Valida os dados antes de salvar e verifica
            se a quantidade de itens no estoque não é negativa.
        """

        if self.quantidade < 0:
            raise ValidationError('A quantidade não pode ser negativa.')

    def __str__(self):
        """
        Retorna uma organização da movimentação de estoque com nome e quantidade.
        """

        return f"{self.produto.nome} - {self.quantidade}"

    class Meta:
        verbose_name = "Movimentação de Estoque"
        verbose_name_plural = "Movimentações de Estoque"
        ordering = ['-data_movimentacao']
