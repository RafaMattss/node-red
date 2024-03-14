from django.db import models

class NoderedModel(models.Model):
    Sensor = models.BooleanField()
    Botao = models.BooleanField()
    LigaRobo = models.BooleanField()
    ResetContador = models.BooleanField()
    Valor_Contagem = models.IntegerField()

    def __str__(self):
        return f"Sensor: {self.Sensor}, Botao: {self.Botao}, LigaRobo: {self.LigaRobo}, ResetContador: {self.ResetContador}, Valor Contagem: {self.Valor_Contagem}"