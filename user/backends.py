from django.contrib.auth.backends import BaseBackend
from user.models import Gerente, Caixa

class GerenteBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Gerente.objects.get(username=username)
            if user.check_password(password):
                return user
        except Gerente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Gerente.objects.get(pk=user_id)
        except Gerente.DoesNotExist:
            return None

class CaixaBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Caixa.objects.get(username=username)
            if user.check_password(password):
                return user
        except Caixa.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Caixa.objects.get(pk=user_id)
        except Caixa.DoesNotExist:
            return None
