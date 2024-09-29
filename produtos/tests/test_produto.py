from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from produtos.models import Produto
from django.contrib.auth.models import User


class ProdutoViewSetTest(APITestCase):

    def setUp(self):
        # Criar um usuário autenticado
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Criar um produto para testar as operações de CRUD
        self.produto = Produto.objects.create(
            nome="Produto Teste",
            codigo=123,
            descricao="Descrição teste",
            valor_venda=100.00
        )

        self.url_list = '/api/produtos/'  # Rota para listar e criar produtos

    def test_list_produtos(self):
        """Testa se a listagem de produtos está funcionando"""
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Deve haver 1 produto criado

    def test_create_produto(self):
        """Testa se um novo produto pode ser criado"""
        data = {
            "nome": "Produto Novo",
            "codigo": 456,
            "descricao": "Novo produto",
            "valor_venda": "200.00",
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 2)  # Deve haver 2 produtos no banco de dados

    def test_update_produto(self):
        """Testa se um produto pode ser atualizado"""
        url_detail = f'/api/produtos/{self.produto.pk}/'  # URL de detalhe do produto
        data = {
            "nome": "Produto Atualizado",
            "codigo": 789,
            "descricao": "Descrição atualizada",
            "valor_venda": "150.00",
        }
        response = self.client.put(url_detail, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, "Produto Atualizado")

    def test_delete_produto(self):
        """Testa se um produto pode ser deletado"""
        url_detail = f'/api/produtos/{self.produto.pk}/'  # URL de detalhe do produto
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produto.objects.count(), 0)

    def test_search_produto(self):
        """Testa se a busca de produto está funcionando"""
        response = self.client.get(self.url_list, {'search': 'Produto Teste'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Deve retornar 1 produto