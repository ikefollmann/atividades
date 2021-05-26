from django.db import models
from datetime import datetime, date
import json

# Create your models here.

class Atividade(models.Model):
    descricao = models.CharField(max_length=100)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()

class Relatorio(models.Model):
    def getDia(dia):
        atividades = Atividade.objects.all()
        data = datetime.strptime(dia, '%Y-%m-%d')
        json = '{'
        for atividade in atividades:
            if atividade.data_inicial.date() <= data.date() <= atividade.data_final.date():
                datedif = datetime.strptime(str(atividade.data_final.time()), '%H:%M:%S') - datetime.strptime(str(atividade.data_inicial.time()), '%H:%M:%S')
                json = json + '"'+str(atividade.id)+'": {"descricao": "'+atividade.descricao+'", "tempo": "'+str(datedif)+'"},'
        json = json[0:-1] + '}'

        return json
