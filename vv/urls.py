from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.viewsets import GerenteViewSet
from produtos.viewsets import ProdutoViewSet, EstoqueViewSet
from vendas.viewsets import VendaViewSet, ItemVendaViewSet
from user.view import login_view, admin_login_redirect, home_view
from vendas.view import caixa_view, gerar_nota_fiscal
from produtos.view import produto_view


router = DefaultRouter()
router.register(r'gerentes', GerenteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'venda', VendaViewSet)
router.register(r'item-venda', ItemVendaViewSet)
urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('caixa/', caixa_view, name='caixa'),
    path('produto/', produto_view, name='produto'),
    path('admin/login/', admin_login_redirect, name='admin_login_redirect'),
    path('gerar-nota-fiscal/<int:venda_id>/', gerar_nota_fiscal, name='gerar_nota_fiscal'),
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
