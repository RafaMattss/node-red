from .models import NoderedModel
from rest_framework.views import APIView
from .serializers import NoderedSerializer
from rest_framework.response import Response
from django.shortcuts import render


class NoderedView(APIView):
    queryset = NoderedModel.objects.all()
    serializer_class = NoderedSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        nodered = NoderedSerializer(
            data={
                "Sensor": data["Sensor"],
                "Botao": data["Botao"],
                "LigaRobo": data["LigaRobo"],
                "ResetContador": data["ResetContador"],
                "Valor_Contagem": data["Valor Contagem"],
            }
        )
        nodered.is_valid(raise_exception=True)
        nodered.save()
        return Response(nodered.data)
        
    def get(self, request, *args, **kwargs):
        last_object = NoderedModel.objects.last()
        serializer = NoderedSerializer(instance=last_object)
        return render(request, 'node.html', {'object': serializer.data})