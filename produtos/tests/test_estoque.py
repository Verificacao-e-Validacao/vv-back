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

    def test_update_estoque(self):
        """Testa se uma movimentação de estoque pode ser atualizada"""
        url_detail = f'/api/estoque/{self.estoque.pk}/'
        data = {
            "produto": self.produto.pk,
            "peso": "15.00",
            "valor_compra": "60.00",
            "quantidade": 80,
            "vencimento": "2025-01-01"
        }
        response = self.client.put(url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.estoque.refresh_from_db()
        self.assertEqual(self.estoque.peso, 15.00)
        self.assertEqual(self.estoque.quantidade, 80)
    
    def test_delete_estoque(self):
        """Testa se uma movimentação de estoque pode ser deletada"""
        url_detail = f'/api/estoque/{self.estoque.pk}/'
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Estoque.objects.count(), 0)