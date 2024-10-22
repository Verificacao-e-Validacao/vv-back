from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from ..models import Venda
from django.shortcuts import render
import tempfile
from django.contrib.auth.decorators import login_required

@login_required
def gerar_nota_fiscal(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    itens_venda = venda.itens.all()

    # Calcula o total para cada item
    for item in itens_venda:
        item.total = item.valor_unitario * item.quantidade

    # Contexto para o template
    context = {
        'venda': venda,
        'itens': itens_venda,
        
    }

    # Renderiza o template em HTML
    html_string = render_to_string('nota_fiscal.html', context)

    # Cria um arquivo temporário para gerar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="nota_fiscal_{venda_id}.pdf"'

    # Usa WeasyPrint para converter o HTML para PDF
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        HTML(string=html_string).write_pdf(target=response)
    
    return response
