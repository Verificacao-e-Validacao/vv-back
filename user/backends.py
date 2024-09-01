from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from user.models import Gerente

class GerenteBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            if user.check_password(password) and isinstance(user, Gerente):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Gerente.objects.get(pk=user_id)
        except Gerente.DoesNotExist:
            return None