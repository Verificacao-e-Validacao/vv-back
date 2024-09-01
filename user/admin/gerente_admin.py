from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import Gerente

@admin.register(Gerente)
class GerenteAdmin(UserAdmin):
    model = Gerente
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
