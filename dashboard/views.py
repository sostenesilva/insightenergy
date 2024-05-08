from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import BdDadosdeAcesso
from .forms import Acesso_form
from django.core.paginator import Paginator

# Create your views here.
@login_required
def dashboard(request):
    bddadosdeacesso = BdDadosdeAcesso.objects.all()

    acesso_paginator = Paginator(bddadosdeacesso,10)
    page_num_acesso = request.GET.get('page_acesso')
    page_acesso = acesso_paginator.get_page(page_num_acesso)

    context = {
        'bd_acesso':page_acesso,
    }

    return render(request,"dashboard/dashpage.html",context)

@login_required
def acesso_add(request):
    acesso_form = Acesso_form(request.POST or None)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if acesso_form.is_valid():
            acesso_form.save() #salva no banco de dados
            return redirect('dashpage') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'acesso_form':acesso_form
    }
    return render(request,"dashboard/acesso_add.html", context)

@login_required
def acesso_edit(request, irrad_pk):
    acesso_item = BdDadosdeAcesso.objects.get(pk=irrad_pk)

    acesso_form = Acesso_form(request.POST or None, instance=acesso_item)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if acesso_form.is_valid():
            acesso_form.save() #salva no banco de dados
            return redirect('dashpage') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'acesso_form':acesso_form
    }
    return render(request,"dashboard/acesso_edit.html", context)

@login_required
def acesso_delet(request, irrad_pk):
    acesso_item = BdDadosdeAcesso.objects.get(pk=irrad_pk)
    acesso_item.delete()
    return redirect('dashpage')