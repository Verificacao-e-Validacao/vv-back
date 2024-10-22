from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from vendas.models import Venda, ItemVenda
from produtos.models import Produto, Estoque
import datetime

class VendaViewSetTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='vendedor', password='12345')
        self.client.login(username='vendedor', password='12345')

        self.vendedor_content_type = ContentType.objects.get_for_model(self.user)

        self.produto = Produto.objects.create(
            nome="Produto Teste", codigo=123, valor_venda=100.00
        )
        self.estoque = Estoque.objects.create(
            produto=self.produto,peso=1,valor_compra=10,quantidade=100,vencimento=datetime.datetime.now()
        )

        self.venda = Venda.objects.create(
            vendedor_content_type=self.vendedor_content_type,
            vendedor_object_id=self.user.id,
            valor_total=0
        )

        self.url_list = '/api/venda/'
        self.url_list_itens_venda = '/api/item-venda/'
    
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

    def test_create_item_venda(self):
        """Testa se um novo item de venda pode ser criado e o valor total da venda atualizado"""
        data = {
            "venda": self.venda.pk,
            "produto": self.produto.pk,
            "quantidade": 2,
            "valor_unitario": "100.00"
        }
        response = self.client.post(self.url_list_itens_venda, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ItemVenda.objects.count(), 1)

        self.venda.refresh_from_db()
        self.assertEqual(self.venda.valor_total, 200.00)
    
    def test_create_item_venda_valor_invalido(self):
        """Testa se a criação de um item de venda com valor inválido é rejeitada"""
        data = {
            "venda": self.venda.pk,
            "produto": self.produto.pk,
            "quantidade": 2,
            "valor_unitario": "-50.00"
        }
        response = self.client.post(self.url_list_itens_venda, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('valor_unitario', response.data)
        self.assertEqual(ItemVenda.objects.count(), 0)

    def test_update_item_venda(self):
        """Testa se um item de venda pode ser atualizado e o valor total da venda recalculado"""
        item_venda = ItemVenda.objects.create(
            venda=self.venda,
            produto=self.produto,
            quantidade=2,
            valor_unitario=100.00
        )
        url_detail_item_venda = f'/api/item-venda/{item_venda.pk}/'
        
        data = {
            "venda": self.venda.pk,
            "produto": self.produto.pk,
            "quantidade": 3,
            "valor_unitario": "100.00"
        }
        response = self.client.put(url_detail_item_venda, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.venda.refresh_from_db()
        self.assertEqual(self.venda.valor_total, 300.00)
    
    def test_valor_total_atualizado_apos_item_venda(self):
        """Testa se o valor total da venda é atualizado corretamente após adicionar um item"""
        # Verifica o valor total inicial da venda
        self.assertEqual(self.venda.valor_total, 0)

        # Dados do item de venda
        data = {
            "venda": self.venda.pk,
            "produto": self.produto.pk,
            "quantidade": 2,
            "valor_unitario": "100.00"
        }

        response = self.client.post(self.url_list_itens_venda, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.venda.refresh_from_db()

        self.assertEqual(self.venda.valor_total, 200.00)
    
    def test_delete_item_venda(self):
        """Testa se um item de venda pode ser deletado e o valor total da venda atualizado"""
        item_venda = ItemVenda.objects.create(
            venda=self.venda,
            produto=self.produto,
            quantidade=2,
            valor_unitario=100.00
        )
        url_detail_item_venda = f'/api/item-venda/{item_venda.pk}/'

        response = self.client.delete(url_detail_item_venda)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.venda.refresh_from_db()
        self.assertEqual(self.venda.valor_total, 0.00)

