from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from user.models import Gerente
from user.serializer import GerenteSerializer


class GerenteViewSet(viewsets.ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
