from rest_framework import serializers

from ..models import Estoque


class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'

    def validate_quantidade(self, value):
        if value < 0:
            raise serializers.ValidationError("A quantidade não pode ser negativa.")
        return value
