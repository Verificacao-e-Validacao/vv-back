from django.contrib import admin

from ..models import ItemVenda


class ItemVendaInline(admin.StackedInline):
    model = ItemVenda

    extra = 0
