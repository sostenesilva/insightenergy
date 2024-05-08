from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def marketing(request):
    return render(request,"marketing/dashmarketing.html")