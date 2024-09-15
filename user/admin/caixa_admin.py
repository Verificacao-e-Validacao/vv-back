from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import Caixa

@admin.register(Caixa)
class CaixaAdmin(UserAdmin):
    model = Caixa
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
