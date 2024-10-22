from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,]

    filterset_fields = {
        'codigo': ["exact"],
    }
