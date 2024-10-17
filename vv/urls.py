from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.viewsets import GerenteViewSet
from produtos.viewsets import ProdutoViewSet, EstoqueViewSet
from vendas.viewsets import VendaViewSet, ItemVendaViewSet


router = DefaultRouter()
router.register(r'gerentes', GerenteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'venda', VendaViewSet)
router.register(r'item-venda', ItemVendaViewSet)
urlpatterns = [
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
