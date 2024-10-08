from django.db import models
from django.db.models import Sum

class Produto(models.Model):
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

        total_quantidade = self.movimentacoes_estoque.aggregate(total=Sum('quantidade'))['total']
        return total_quantidade or 0 

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "produtos"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
