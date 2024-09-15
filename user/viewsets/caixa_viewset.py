from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from user.models import Caixa
from user.serializers import CaixaSerializer


class CaixaViewSet(viewsets.ModelViewSet):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
