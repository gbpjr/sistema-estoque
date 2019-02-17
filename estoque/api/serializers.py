from rest_framework import serializers
from estoque.models import Componente

class ComponenteSerializer(serializers.ModelSerializer):
    tipo = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nome'
    )

    local = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nome'
    )

    fabricante = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nome'
    )

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
