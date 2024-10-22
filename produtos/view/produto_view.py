from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.produto import Produto
@login_required
def produto_view(request):
    return render(request, 'produtos.html')


@login_required
def estoque_view(request, id):
    context = {
        "produto": Produto.objects.get(id=id)
    }
    return render(request, 'estoque.html', context )