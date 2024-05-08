from django import forms
from .models import BdDadosdeAcesso
from django.utils.timezone import now


class Acesso_form (forms.ModelForm):
    class Meta:
        model = BdDadosdeAcesso
        fields = ('fornecedor','login','senha','link','level','atualizacao')
        
        widgets = {
            'fornecedor': forms.TextInput(attrs={'class':'form-control','autofocus':'','placeholder':'Nome do fornecedor do serviço'}),
            'login': forms.TextInput(attrs={'class':'form-control','autofocus':'','placeholder':'Login de acesso'}),
            'senha': forms.TextInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'Senha de acesso'}),
            'link': forms.URLInput(attrs={'class':'form-control','autofocus':'', 'placeholder':'https://endereço_de_login.fornecedor.com.br'}),
            'level': forms.Select(attrs={'class':'form-control','autofocus':'', 'placeholder':'Autorização'}),            
            'atualizacao': forms.DateInput(attrs={'class':'form-control','autofocus':'', 'value': now}),
        }