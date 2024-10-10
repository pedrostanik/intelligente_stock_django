from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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

def check_storage(request, currentValue, productId):
    produto = get_object_or_404(Produtos, id=productId)
    if (produto.quantidade > currentValue):
        return JsonResponse({'disponivel': True, 'quantidade': produto.quantidade})
    else:
        return JsonResponse({'disponivel': False, 'quantidade': produto.quantidade})


# def add_to_cart(request):
#     if (request.method == 'POST'):
#         product_id = request.POST.get('product_id')
#         quantity = request.POST.get('qtty_product')

#         product = get_object_or_404(Produtos, id=product_id)
#         cart = request.session.get('cart')

#         if product_id in cart:
#             cart[product_id]['quantidade'] += quantidade
#         else:
#             cart[product_id] = {'nome': product.nome, 'preco': product.preco, 'quantidade': product.quantidade}
        
#         request.session['cart'] = cart
#     return redirect('cart')

def cart(request): 
    print(f'request.method: {request.method}')   
    product_id = request.POST.getlist('product_id')
    quantity = request.POST.getlist('qttyProduct')
    print(f'product_id: {product_id}')
    print(f'quantity: {quantity}')
    return render(request, 'produtos/cart.html')

    
    


