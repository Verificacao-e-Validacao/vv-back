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
