from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def homePage(request):
    return render(request,'home.html')

def sair(request):
    return render(request,'saiu.html')