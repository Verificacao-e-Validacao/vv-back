from rest_framework import serializers

from ..models import Venda


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

    def validate_valor_total(self, value):
        '''Valida se o valor_total é negativo.'''
        if value < 0:
            raise serializers.ValidationError('O valor total não pode ser negativo.')
        return value
