from rest_framework import serializers

from user.models import Gerente


class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = '__all__'
