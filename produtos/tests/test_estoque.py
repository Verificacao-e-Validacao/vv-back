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

        self.url_list = '/api/estoque/'
    
    def test_list_estoques(self):
        """Testa se a listagem de estoques está funcionando"""
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_create_estoque(self):
        """Testa se uma nova movimentação de estoque pode ser criada"""
        data = {
            "produto": self.produto.pk,
            "peso": "5.75",
            "valor_compra": "25.00",
            "quantidade": 50,
            "vencimento": "2024-12-31"
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estoque.objects.count(), 2)