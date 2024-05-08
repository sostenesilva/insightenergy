from django.db import models
from django.utils.timezone import now


# Create your models here.
class Irradiacao (models.Model):
    uf = models.CharField('Estado',blank=False,max_length=2,default='PE')
    cidade = models.CharField(blank=False,max_length=50)
    irr = models.TextField('Irradiação',blank=True)
    irr_jan = models.FloatField(default=0)
    irr_fev = models.FloatField(default=0)
    irr_mar = models.FloatField(default=0)
    irr_abr = models.FloatField(default=0)
    irr_mai = models.FloatField(default=0)
    irr_jun = models.FloatField(default=0)
    irr_jul = models.FloatField(default=0)
    irr_ago = models.FloatField(default=0)
    irr_set = models.FloatField(default=0)
    irr_out = models.FloatField(default=0)
    irr_nov = models.FloatField(default=0)
    irr_dez = models.FloatField(default=0)
    irr_media = models.FloatField(default=0)
    atualizacao = models.DateField('Última atualização',default=now)

    def __str__(self):
        return '{} - {}'.format(self.cidade,self.uf)

class Bd_Modulos(models.Model):
    marca = models.CharField(max_length=300)
    modelo = models.TextField()
    potencia = models.PositiveIntegerField()
    eficiencia = models.FloatField()
    area = models.FloatField()
    peso = models.FloatField()
    atualizacao = models.DateField('Última Atualização',default=now)

    def __str__(self):
        return '{} - {}Wp - {}'.format(self.marca,self.potencia,self.modelo)

class Bd_Inversor(models.Model):
    tipo = models.CharField(max_length=10,choices={'micro':'Micro Inversor', 'inversor':'Inversor'})
    marca = models.CharField(max_length=300)
    modelo = models.TextField()
    potencia = models.PositiveIntegerField()
    atualizacao = models.DateField('Última Atualização',default=now)

    def __str__(self):
        return '{} - {}kW - {}'.format(self.marca,self.potencia,self.modelo)

class Bancodeprecos(models.Model):
    inversor = models.ForeignKey(Bd_Inversor,on_delete=models.CASCADE)
    modulo = models.ForeignKey(Bd_Modulos,on_delete=models.CASCADE)
    qtdModulos = models.PositiveIntegerField('Quantidade de Módulos',default=0)
    qtdInversor = models.PositiveIntegerField('Quantidade de Inversores',default=0)
    potencia = models.IntegerField('Potência',blank=False)
    preco = models.FloatField('Preço',blank=False)
    fornecedor = models.TextField(blank=False)
    link = models.URLField(blank=True)
    atualizacao = models.DateField('Última Atualização',default=now)

    def __str__(self):
        return '{} - {}kW - {}'.format(self.marca,self.potencia,self.modelo)


class Bd_propostas (models.Model):
    cliente = models.CharField(max_length=300)
    telefone = models.CharField(max_length=50)
    uf = models.ForeignKey(Irradiacao,on_delete=models.CASCADE,related_name='uf_irr')
    cidade = models.ForeignKey(Irradiacao,on_delete=models.CASCADE,related_name='cidade_irr')
    data = models.DateField('Data da Proposta',default=now)
    consumo = models.PositiveIntegerField('Consumo Faturado')
    ligacao = models.CharField(max_length=5,choices={'mono':'monofásico','tri':'trifásico'})
    equipamentos = models.FloatField('Equipamentos Elétricos')
    impostos = models.FloatField()
    equipe = models.FloatField('Custo com Equipe de execução')
    captador = models.FloatField('Porcentagem do captador')
    lucro = models.FloatField('Lucro Previsto')
    valor_final = models.FloatField('Valor final do Projeto')
    preco_sugerido = models.FloatField('Preço Sugerido')
    payback = models.TextField('Retorno Financeiro')
