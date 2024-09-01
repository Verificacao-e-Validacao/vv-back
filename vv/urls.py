from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.viewsets import GerenteViewSet
from produtos.viewsets import ProdutoViewSet

router = DefaultRouter()
router.register(r'gerentes', GerenteViewSet)
router.register(r'produtos', ProdutoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
