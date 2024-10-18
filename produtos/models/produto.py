from django.db import models
from django.db.models import Sum

class Produto(models.Model):
    """
    Representa um produto disponível no sistema de gerenciamento.

    """

    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    codigo = models.IntegerField(
        verbose_name="Código",
    )

    descricao = models.TextField(
        verbose_name="Descrição", 
        blank=True, null=True,
        help_text="Descrição do produto"
    )

    valor_venda = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Valor de venda do produto"
    )

    detalhes = models.TextField(
        blank=True, null=True, help_text="Detalhes adicionais sobre o produto"
    )

    @property
    def total_estoque(self):
        """
        Calcula o total de itens em estoque para este produto.

        O total é calculado somando todas as movimentações de estoque associadas ao produto.
        Se não houver movimentações, retorna 0.
        """
        total_quantidade = self.movimentacoes_estoque.aggregate(total=Sum('quantidade'))['total']
        return total_quantidade or 0 

    def __str__(self):
        """
        Retorna uma string representando o produto.

        """
        return self.nome

    class Meta:
        """
        Define as configurações meta do modelo Produto.
        
        """
        app_label = "produtos"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
