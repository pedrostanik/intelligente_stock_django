from django.shortcuts import render
from .models import Produtos
from django.http import HttpResponse
import datetime
from chatbot.assistant_gpt import AssistantGPT

def get_products(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos/index.html', {'produtos': produtos})

def petshop(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos/petshop.html', {'produtos': produtos})

def banho_tosa(request):
    return render(request, 'produtos/banho_tosa.html')

def creche(request):
    return render(request, 'produtos/creche.html')

def register_product(request):
    nome = request.GET.get('nome')
    preco = request.GET.get('preco')
    quantidade = request.GET.get('quantidade')
    descricao = request.GET.get('descricao')
    data_atualizacao = datetime.datetime.now()

    if (nome and preco and quantidade and data_atualizacao and descricao):
        produto = Produtos(nome=nome, preco=preco, quantidade=quantidade, data_atualizacao=data_atualizacao, descricao=descricao)
        produto.save()
        return HttpResponse(f'Produto {nome} inserido com sucesso!')
    return HttpResponse(f'Erro no registro!')

def respond_message(request, message):
    assistant_gpt = AssistantGPT()
    answer = assistant_gpt.execute(message)
    return HttpResponse(answer)
    


