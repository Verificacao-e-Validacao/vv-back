from django.contrib import admin

from ..models import Estoque


class EstoqueInline(admin.StackedInline):
    model = Estoque
    extra = 0
