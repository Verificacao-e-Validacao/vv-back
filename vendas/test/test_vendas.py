from django.test import TestCase
from produtos.models import Produto
from vendas.models import Venda
from decimal import Decimal


class VendaViewSetTestCase(TestCase):

    def setUp(self):
        # Criação de objetos Produto para serem usados nos testes
        self.produto1 = Produto.objects.create(
            nome="Produto Teste 1",
            codigo=1001,
            descricao="Descrição do Produto Teste 1",
            valor_venda=Decimal('10.00')
        )

        self.produto2 = Produto.objects.create(
            nome="Produto Teste 2",
            codigo=1002,
            descricao="Descrição do Produto Teste 2",
            valor_venda=Decimal('20.00')
        )

        # Criação de uma venda
        self.venda = Venda.objects.create(
            cliente="Cliente Teste",
            data_venda="2024-10-13"
        )

    def test_criacao_produto(self):
        """Testa a criação de produtos no banco de dados"""
        self.assertEqual(Produto.objects.count(), 2)
        self.assertEqual(self.produto1.nome, "Produto Teste 1")
        self.assertEqual(self.produto2.valor_venda, Decimal('20.00'))