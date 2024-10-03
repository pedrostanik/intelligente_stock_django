from django.shortcuts import render
from .models import Produtos
from django.http import HttpResponse

def get_products(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos/index.html')
