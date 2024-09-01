from django.contrib.auth.backends import BaseBackend
from user.models import Gerente

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
