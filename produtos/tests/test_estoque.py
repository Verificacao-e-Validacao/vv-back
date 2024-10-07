from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from produtos.models import Produto, Estoque
from django.urls import reverse
from datetime import date

class EstoqueViewSetTest(APITestCase):
    
    def setUp(self):
        # Criar um usuário autenticado
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Criar um produto de teste
        self.produto = Produto.objects.create(
            nome="Produto Teste",
            codigo=123,
            descricao="Descrição teste",
            valor_venda=100.00
        )

        # Criar uma movimentação de estoque para testes
        self.estoque = Estoque.objects.create(
            produto=self.produto,
            peso=10.50,
            valor_compra=50.00,
            quantidade=100,
            vencimento=date(2024, 12, 31)
        )

        self.url_list = '/api/estoques/'