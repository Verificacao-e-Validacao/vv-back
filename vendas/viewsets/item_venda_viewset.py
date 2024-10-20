from rest_framework import filters, viewsets
from django_filters import rest_framework as django_filters
from rest_framework.permissions import IsAuthenticated

from ..models import ItemVenda
from ..serializers import ItemVendaSerializer

class ItemVendaFilter(django_filters.FilterSet):
    venda = django_filters.NumberFilter(field_name='venda__id')

    class Meta:
        model = ItemVenda
        fields = ['venda']

class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ItemVendaFilter

    search_fields = [

    ]
