from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vendas.models import Venda

@login_required(login_url='/login/') 
def caixa_view(request):
    venda_id = request.GET.get("venda")
    try:
        venda = Venda.objects.get(id=venda_id)
    except:
        return redirect('/')
    return render(request, 'caixa.html', {'venda': venda})