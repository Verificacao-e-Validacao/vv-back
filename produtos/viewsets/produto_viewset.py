from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
