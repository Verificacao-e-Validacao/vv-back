from django.contrib import admin

from ..models import Venda


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
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

    readonly_fields = ['data_venda']
