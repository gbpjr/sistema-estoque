from rest_framework import serializers
from estoque.models import Componente

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = [
            'nome',
            'quantidade',
            'aplicacao',
            'tipo',
            'local',
            'fabricante',
        ]
