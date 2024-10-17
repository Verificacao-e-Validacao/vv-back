from rest_framework import serializers

from ..models import ItemVenda


class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = '__all__'

    def validate_valor_unitario(self, value):
        '''Valida se o valor_unitario é negativo.'''
        if value < 0:
            raise serializers.ValidationError('O valor unitario não pode ser negativo.')
        return value
