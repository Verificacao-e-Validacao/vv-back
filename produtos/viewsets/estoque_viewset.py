from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Estoque
from produtos.serializers import EstoqueSerializer


class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]
