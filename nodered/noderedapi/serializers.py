from rest_framework import serializers
from .models import NoderedModel

class NoderedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoderedModel
        fields = ['id', 'Sensor', 'Botao', 'LigaRobo', 'ResetContador', 'Valor_Contagem']