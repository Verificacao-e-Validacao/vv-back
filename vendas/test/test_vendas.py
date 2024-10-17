from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from vendas.models import Venda
from produtos.models import Produto

class VendaViewSetTest(APITestCase):

    def setUp(self):
        # Criar um usuário autenticado para ser o vendedor
        self.user = User.objects.create_user(username='vendedor', password='12345')
        self.client.login(username='vendedor', password='12345')

        # Criar a ContentType do vendedor
        self.vendedor_content_type = ContentType.objects.get_for_model(self.user)

        # Criar uma venda de teste
        self.venda = Venda.objects.create(
            vendedor_content_type=self.vendedor_content_type,
            vendedor_object_id=self.user.id,
            valor_total=0
        )

        # URL para a listagem de vendas
        self.url_list = '/api/venda/'
    
    def test_list_vendas(self):
        """Testa se a listagem de vendas está funcionando"""
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_venda(self):
        """Testa se uma nova venda pode ser criada"""
        data = {
            "vendedor_content_type": self.vendedor_content_type.id,
            "vendedor_object_id": self.user.id,
            "valor_total": "200.00"
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Venda.objects.count(), 2)
    
    def test_create_venda_valor_invalido(self):
        """Testa se a criação de uma venda com valor inválido é rejeitada"""
        data = {
            "vendedor_content_type": self.vendedor_content_type.id,
            "vendedor_object_id": self.user.id,
            "valor_total": "-50.00"
        }
        response = self.client.post(self.url_list, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('valor_total', response.data)
        self.assertEqual(Venda.objects.count(), 1)