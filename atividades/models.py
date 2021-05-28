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
        dados = []
        for atividade in atividades:
            id = []
            ativ = []
            aux = []
            if atividade.data_inicial.date() <= data.date() <= atividade.data_final.date():
                datedif = datetime.strptime(str(atividade.data_final.time()), '%H:%M:%S') - datetime.strptime(str(atividade.data_inicial.time()), '%H:%M:%S')

                id.append(atividade.id)

                ativ.append(atividade.descricao)
                ativ.append(datedif)

                aux.append(id)
                aux.append(ativ)

                dados.append(aux)

        return dados

    def getRel(descricao):
        atividades = Atividade.objects.all()
        adicionados = []
        dados = []
        for atividade in atividades:
            id = []
            ativ = []
            aux = []
            if atividade not in adicionados and atividade.descricao == descricao:
                adicionados.append(atividade)
                datedif = datetime.strptime(str(atividade.data_final.time()), '%H:%M:%S') - datetime.strptime(str(atividade.data_inicial.time()), '%H:%M:%S')

                id.append(atividade.id)

                ativ.append(atividade.data_inicial)
                ativ.append(datedif)

                aux.append(id)
                aux.append(ativ)

                dados.append(aux)

        return dados
