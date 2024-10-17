from django.contrib import admin

from ..models import Venda
from ..forms import VendaForm
from .item_venda_inline import ItemVendaInline

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):

    inlines = [ItemVendaInline]
    list_display = [
        'id',
        'vendedor',
        'valor_total',
        'data_venda',
    ]

    search_fields = [
        'id',
        'vendedor',
    ]

    form = VendaForm

    readonly_fields = ['data_venda']
