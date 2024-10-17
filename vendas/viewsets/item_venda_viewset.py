from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import ItemVenda
from .arquivo_serializer import ItemVendaSerializer


class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]
