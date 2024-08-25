from django.contrib import admin
from produtos.models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'codigo',
    ]

    search_fields = [
        'id',
        'nome',
        'codigo',
    ]
