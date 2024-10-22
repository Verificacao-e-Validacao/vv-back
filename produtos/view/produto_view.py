from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def produto_view(request):
    return render(request, 'produtos.html')