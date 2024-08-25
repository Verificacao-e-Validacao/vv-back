from django.db import models


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

    peso = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Peso do produto em quilogramas",
    )

    valor_compra = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Valor de compra do produto"
    )

    valor_venda = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Valor de venda do produto"
    )

    quantidade = models.IntegerField(
        help_text="Quantidade disponível em estoque"
    )

    vencimento = models.DateField(
        help_text="Data de vencimento do produto"
    )

    detalhes = models.TextField(
        blank=True, null=True, help_text="Detalhes adicionais sobre o produto"
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "produtos"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
