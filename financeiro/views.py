from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def financeiro(request):
    return render(request,"financeiro/dashfinanceiro.html")
