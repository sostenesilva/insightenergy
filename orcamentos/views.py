from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import Inversor_form, Irrad_form, Modulo_form, Precos_form
from .models import Irradiacao, Bancodeprecos, Bd_Inversor, Bd_Modulos, Bd_propostas
from django.core.paginator import Paginator


# VIEWS PARA MODEL ORÇAMENTOS
@login_required
def orcamentos(request):
    return render(request,"orcamentos/dashorcamentos.html")

@login_required
def historico_orcamentos(request):
    return render(request,"orcamentos/historico_orcamentos.html")


# VIEWS PARA A MODEL BANCO DE EQUIPAMENTOS
@login_required
def bancodeequipamentos(request):
    bd_inversor = Bd_Inversor.objects.all()
    bd_modulos = Bd_Modulos.objects.all()

    inversor_paginator = Paginator(bd_inversor,10)
    page_num_inv = request.GET.get('page_inv')
    page_inv = inversor_paginator.get_page(page_num_inv)

    modulo_paginator = Paginator(bd_modulos,10)
    page_num_mod = request.GET.get('page_mod')
    page_mod = modulo_paginator.get_page(page_num_mod)

    context = {
        'bd_inversor':page_inv,
        'bd_modulos':page_mod,
    }

    return render(request,"orcamentos/bancodeequipamentos.html",context)

@login_required
def inversor_add(request):
    inversor_form = Inversor_form(request.POST or None)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if inversor_form.is_valid():
            inversor_form.save() #salva no banco de dados
            return redirect('banco_de_equipamentos') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'inversor_form':inversor_form
    }
    return render(request,"orcamentos/inversor_add.html", context)

@login_required
def modulo_add(request):
    modulo_form = Modulo_form(request.POST or None)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if modulo_form.is_valid():
            modulo_form.save() #salva no banco de dados
            return redirect('banco_de_equipamentos') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'modulo_form':modulo_form
    }
    return render(request,"orcamentos/modulo_add.html", context)

@login_required
def inversor_edit(request, inversor_pk):
    inversor_item = Bd_Inversor.objects.get(pk=inversor_pk)

    inversor_form = Inversor_form(request.POST or None, instance=inversor_item)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if inversor_form.is_valid():
            inversor_form.save() #salva no banco de dados
            return redirect('banco_de_equipamentos') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'inversor_form':inversor_form
    }
    return render(request,"orcamentos/inversor_edit.html", context)

@login_required
def modulo_edit(request, modulo_pk):
    modulo_item = Bd_Modulos.objects.get(pk=modulo_pk)

    modulo_form = Modulo_form(request.POST or None, instance=modulo_item)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if modulo_form.is_valid():
            modulo_form.save() #salva no banco de dados
            return redirect('banco_de_equipamentos') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'modulo_form':modulo_form
    }
    return render(request,"orcamentos/modulo_edit.html", context)

@login_required
def inversor_delet(request, inversor_pk):
    inversor_item = Bd_Inversor.objects.get(pk=inversor_pk)
    inversor_item.delete()
    return redirect('banco_de_equipamentos')

@login_required
def modulo_delet(request, modulo_pk):
    modulo_item = Bd_Modulos.objects.get(pk=modulo_pk)
    modulo_item.delete()
    return redirect('banco_de_equipamentos')

# VIEWS PARA A MODEL BANCO DE IRRADIAÇÃO
@login_required
def bancodeirradiacao(request):
    bdirradicacao = Irradiacao.objects.all()

    irrad_paginator = Paginator(bdirradicacao,10)
    page_num = request.GET.get('page')
    page = irrad_paginator.get_page(page_num)

    context = {
        'bdirradiacao':page,
    }
    return render(request,"orcamentos/bancodeirradiacao.html",context)


@login_required
def irrad_add(request):
    irrad_form = Irrad_form(request.POST or None)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if irrad_form.is_valid():
            irrad_form.instance.uf = irrad_form.instance.uf.upper() #UF em maíusculo sempre
            
            irr_anual = str(irrad_form.instance.irr).split() #converte a entrada das irradiações numa lista

            #separa a lista em irradiações mensais
            irrad_form.instance.irr_jan = float(irr_anual[0].replace(',','.')) 
            irrad_form.instance.irr_fev = float(irr_anual[1].replace(',','.'))
            irrad_form.instance.irr_mar = float(irr_anual[2].replace(',','.'))
            irrad_form.instance.irr_abr = float(irr_anual[3].replace(',','.'))
            irrad_form.instance.irr_mai = float(irr_anual[4].replace(',','.'))
            irrad_form.instance.irr_jun = float(irr_anual[5].replace(',','.'))
            irrad_form.instance.irr_jul = float(irr_anual[6].replace(',','.'))
            irrad_form.instance.irr_ago = float(irr_anual[7].replace(',','.'))
            irrad_form.instance.irr_set = float(irr_anual[8].replace(',','.'))
            irrad_form.instance.irr_out = float(irr_anual[9].replace(',','.'))
            irrad_form.instance.irr_nov = float(irr_anual[10].replace(',','.'))
            irrad_form.instance.irr_dez = float(irr_anual[11].replace(',','.'))
            irrad_form.instance.irr_media = float(irr_anual[12].replace(',','.'))

            irrad_form.save() #salva no banco de dados
            return redirect('banco_de_irradiacao') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'irrad_form':irrad_form
    }
    return render(request,"orcamentos/irrad_add.html", context)

@login_required
def irrad_edit(request, irrad_pk):
    irrad_item = Irradiacao.objects.get(pk=irrad_pk)

    irrad_form = Irrad_form(request.POST or None, instance=irrad_item)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if irrad_form.is_valid():
            irrad_form.instance.uf = irrad_form.instance.uf.upper() #UF em maíusculo sempre

            irr_anual = str(irrad_form.instance.irr).split() #converte a entrada das irradiações numa lista

            #separa a lista em irradiações mensais
            irrad_form.instance.irr_jan = float(irr_anual[0].replace(',','.')) 
            irrad_form.instance.irr_fev = float(irr_anual[1].replace(',','.'))
            irrad_form.instance.irr_mar = float(irr_anual[2].replace(',','.'))
            irrad_form.instance.irr_abr = float(irr_anual[3].replace(',','.'))
            irrad_form.instance.irr_mai = float(irr_anual[4].replace(',','.'))
            irrad_form.instance.irr_jun = float(irr_anual[5].replace(',','.'))
            irrad_form.instance.irr_jul = float(irr_anual[6].replace(',','.'))
            irrad_form.instance.irr_ago = float(irr_anual[7].replace(',','.'))
            irrad_form.instance.irr_set = float(irr_anual[8].replace(',','.'))
            irrad_form.instance.irr_out = float(irr_anual[9].replace(',','.'))
            irrad_form.instance.irr_nov = float(irr_anual[10].replace(',','.'))
            irrad_form.instance.irr_dez = float(irr_anual[11].replace(',','.'))
            irrad_form.instance.irr_media = float(irr_anual[12].replace(',','.'))

            irrad_form.save() #salva no banco de dados
            return redirect('banco_de_irradiacao') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'irrad_form':irrad_form
    }
    return render(request,"orcamentos/irrad_edit.html", context)

@login_required
def irrad_delet(request, irrad_pk):
    irrad_item = Irradiacao.objects.get(pk=irrad_pk)
    irrad_item.delete()
    return redirect('banco_de_irradiacao')


# VIEWS PARA A MODEL BANCO DE PREÇOS
@login_required
def bancodeprecos(request):
    bdprecos = Bancodeprecos.objects.all()

    precos_paginator = Paginator(bdprecos,10)
    page_num_precos = request.GET.get('page_preco')
    page_preco = precos_paginator.get_page(page_num_precos)

    context = {
        'bdprecos':page_preco,
    }
    return render(request,"orcamentos/bancodeprecos.html",context)



@login_required
def bdprecos_add(request):
    precos_form = Precos_form(request.POST or None)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if precos_form.is_valid():
            precos_form.save() #salva no banco de dados
            return redirect('banco_de_precos') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'precos_form':precos_form
    }
    return render(request,"orcamentos/bdprecos_add.html", context)

@login_required
def bdprecos_edit(request, precos_pk):
    precos_item = Bancodeprecos.objects.get(pk=precos_pk)

    precos_form = Precos_form(request.POST or None, instance=precos_item)
    
    #Se a requisição for do tipo POST
    if request.POST:
        if precos_form.is_valid():
            precos_form.save() #salva no banco de dados
            return redirect('banco_de_precos') #redireciona para a página de consulta do bd

    #Se a requisição não for do tipo POST, renderize a página com o formulário.
    context = {
        'precos_form':precos_form
    }
    return render(request,"orcamentos/bdprecos_edit.html", context)

@login_required
def bdprecos_delet(request, precos_pk):
    precos_item = Bancodeprecos.objects.get(pk=precos_pk)
    precos_item.delete()
    return redirect('banco_de_precos')

    
