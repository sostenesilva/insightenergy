from django.db import models
from django.utils.timezone import now

class BdDadosdeAcesso(models.Model):
    fornecedor = models.CharField('Fornecedor/Serviço',max_length=50)
    login = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)
    link = models.URLField()
    level = models.CharField(max_length=15, choices={'gerente':'Gerência','efetivo':'Efetivos','estagiario':'Estagiários'})
    atualizacao = models.DateField('Atualização',default=now)

