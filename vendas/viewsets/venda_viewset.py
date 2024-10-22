from rest_framework import filters, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Venda, ItemVenda
from ..serializers import VendaSerializer
from produtos.models import Produto
from rest_framework.decorators import action

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def adicionar_produto(self, request, pk=None):
        produto_codigo = request.data.get('codigo_produto')
        quantidade = int(request.data.get('quantidade'))

        try:
            produto = Produto.objects.get(codigo=produto_codigo)
        except Produto.DoesNotExist:
            return Response({"detail": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            venda_atual = Venda.objects.get(pk=pk)
        except Venda.DoesNotExist:
            return Response({"detail": "Venda não encontrada ou já finalizada."}, status=status.HTTP_404_NOT_FOUND)

        try:
            item_venda = ItemVenda.objects.create(venda=venda_atual,produto=produto,quantidade=quantidade,valor_unitario=produto.valor_venda)
        except Exception as e:
            print("Erro item venda",e)
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
        venda_atual.save()

        serializer = VendaSerializer(venda_atual)

        return Response(serializer.data, status=status.HTTP_200_OK)