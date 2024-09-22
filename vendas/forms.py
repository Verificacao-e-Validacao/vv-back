from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import Venda
from user.models import Caixa, Gerente

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendedor_content_type', 'vendedor_object_id', 'valor_total', 'produto', 'quantidade_venda']

    def __init__(self, *args, **kwargs):
        super(VendaForm, self).__init__(*args, **kwargs)
        caixa_type = ContentType.objects.get_for_model(Caixa)
        gerente_type = ContentType.objects.get_for_model(Gerente)
        self.fields['vendedor_content_type'].queryset = ContentType.objects.filter(id__in=[caixa_type.id, gerente_type.id])
