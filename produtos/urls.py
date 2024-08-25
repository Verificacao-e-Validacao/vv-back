from django.urls import path
from produtos.viewsets import ProdutoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = router.urls
