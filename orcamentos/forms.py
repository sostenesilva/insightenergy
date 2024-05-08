from django import forms
from .models import Irradiacao, Bancodeprecos, Bd_Inversor, Bd_Modulos, Bd_propostas
from django.utils.timezone import now


class Irrad_form (forms.ModelForm):
    class Meta:
        model = Irradiacao
        fields = ('uf','cidade','irr','atualizacao')

        widgets = {
            'uf': forms.TextInput(attrs={'class':'form-control','autofocus':'','placeholder':'UF'}),
            'cidade': forms.TextInput(attrs={'class':'form-control','autofocus':'','placeholder':'Nome completo da cidade'}),
            'irr': forms.TextInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'jan   fev   mar   abr   mai   jun   jul   ago   set   out   nov   dez   media'}),
            'atualizacao': forms.DateInput(attrs={'class':'form-control','autofocus':'', 'value': now}),
            
        }

class Precos_form (forms.ModelForm):
    class Meta:
        model = Bancodeprecos
        fields = ('inversor','qtdInversor','modulo','qtdModulos','potencia','preco','fornecedor','link','atualizacao')

        widgets = {
            'inversor': forms.Select(attrs={'class':'form-control','autofocus':''}),
            'qtdInversor': forms.NumberInput(attrs={'class':'form-control','autofocus':''}),
            'qtdModulos': forms.NumberInput(attrs={'class':'form-control','autofocus':''}),
            'modulo': forms.Select(attrs={'class':'form-control','autofocus':''}),
            'potencia': forms.NumberInput(attrs={'class':'form-control','autofocus':'','placeholder':'Potência do kit em kWp'}),
            'preco': forms.NumberInput(attrs={'class':'form-control','autofocus':'','placeholder':'Preço do kit em R$'}),
            'fornecedor': forms.TextInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Nome do fornecedor'}),
            'link': forms.URLInput(attrs={'class':'form-control','autofocus':'','placeholder':'Link do kit para consulta'}),
            'atualizacao': forms.DateInput(attrs={'class':'form-control','autofocus':'', 'value': now}),
        }

class Inversor_form (forms.ModelForm):
    class Meta:
        model = Bd_Inversor
        fields = ('tipo','marca','modelo','potencia', 'atualizacao')

        widgets = {
            'tipo': forms.Select(attrs={'class':'form-control','autofocus':'','placeholder':'Inversor ou Micro?'}),
            'marca': forms.TextInput(attrs={'class':'form-control','autofocus':'','placeholder':'Marca do Inversor'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Modelo do Inversor'}),
            'potencia': forms.NumberInput(attrs={'class':'form-control','autofocus':''}),
            'atualizacao': forms.DateInput(attrs={'class':'form-control','autofocus':'', 'value': now}),  
        }

class Modulo_form (forms.ModelForm):
    class Meta:
        model = Bd_Modulos
        fields = ('marca','modelo','potencia', 'eficiencia','area','peso','atualizacao')

        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control','autofocus':'','placeholder':'Marca do módulo'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Modelo do módulo'}),
            'potencia': forms.NumberInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Potência em kWp'}),
            'eficiencia': forms.NumberInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Eficiência do módulo em %'}),
            'area': forms.NumberInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Área do módulo em m²'}),
            'peso': forms.NumberInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Peso do módulo em Kg'}),    
            'atualizacao': forms.DateInput(attrs={'class':'form-control','autofocus':'', 'value': now}),  
        }