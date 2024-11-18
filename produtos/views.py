from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Produtos, ItemBuy, Buy
from django.http import HttpResponse
import datetime
from concurrent.futures import ThreadPoolExecutor
import asyncio
from chatbot.assistant_gpt import AssistantGPT

from prediction.item_prediction import ItemPrediciton
def get_products(request):
    produtos = Produtos.objects.all()
    return render(request, 'produtos/index.html', {'produtos': produtos})

def petshop(request):
    print(request.method)
    if (request.method == 'GET'):
        if 'campoPesquisa' in request.GET:
            search = request.GET['campoPesquisa']
            print(f'search: {search}')
            produtos = Produtos.objects.filter(descricao__icontains = search)
            return render(request, 'produtos/petshop.html', {'produtos': produtos})
        else:
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


def add_cart(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        produto_id = int(produto_id)
        quantidade = int(request.POST.get('quantidade'))
        print(f'produto_id: {produto_id}')
        print(f'quantidade: {quantidade}')

        # Obtenha o produto pelo ID
        produto = Produtos.objects.get(id=produto_id)

        # Verifique se o carrinho já existe na sessão
        carrinho = request.session.get('carrinho', {})

        # Adicione ou atualize a quantidade do produto no carrinho
        if produto_id in carrinho:
            carrinho[produto_id] += quantidade
        else:
            carrinho[produto_id] = quantidade

        # Atualize a sessão com o carrinho atualizado
        request.session['carrinho'] = carrinho
        print(f'[add_cart]request.session: {request.session}')

        # Redirecione para a página do carrinho
        return redirect('cart')
    else:
        return HttpResponseNotFound('Método não permitido.')


@login_required
def cart(request):
    # Obtenha o carrinho da sessão
    # if not request.user.is_authenticated:
    #     messages.error(request, 'Usuário não logado!')
    #     return redirect('login')
    carrinho = request.session.get('carrinho', {})
    print(f'[cart]carrinho: {carrinho}')

    # Obtenha os produtos do carrinho
    produtos_no_carrinho = Produtos.objects.filter(id__in=carrinho.keys())
    print(f'produtos_no_carrinho: {produtos_no_carrinho}')

    # Crie uma lista com informações dos produtos e suas quantidades
    produtos_carrinho = []
    total = 0  # variável para armazenar o total da compra

    for produto in produtos_no_carrinho:
        quantidade = carrinho.get(str(produto.id))  # pegue a quantidade do produto
        subtotal = produto.preco * quantidade
        total += subtotal
        produtos_carrinho.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal
        })

    # Renderize o template com a lista processada
    return render(request, 'produtos/cart.html', {
        'produtos_carrinho': produtos_carrinho,
        'total': total
    })

def bougth_finished(request):
    return render(request, 'produtos/bougth_finished.html')

def insert_sell(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "É necessário logar para efetuar essa compra!")
            return redirect('login')        
        
        data = datetime.datetime.now()
        week_day = data.strftime('%A')
        month_day = data.day
        weekend = data.weekday() >= 5  # 5 = Sábado, 6 = Domingo
        
        total_produtos = int(request.POST.get('total_produtos'))
        total_value = 0
        for i in range(1, total_produtos+1):
            produto_subtotal = float(request.POST.get('produto_subtotal_' + str(i)))
            total_value+=produto_subtotal

        print(f'total_value: {total_value}')
        print(request.user.username)
        buy = Buy(
            user = request.user,
            week_day = week_day,
            month_day = month_day,
            weakend = weekend,
            total = total_value,
        )
        buy.save()

        if (not buy):
            messages.error('Erro ao realizar compra!')
            return redirect('home')
        
        # Criar os objetos ItemCompra
        for i in range(1, total_produtos+1):            
            produto_nome = request.POST.get('produto_nome_' + str(i))
            produto = Produtos.objects.get(nome=produto_nome)
            produto_quantidade = request.POST.get('produto_quantidade_' + str(i))
            produto_preco = request.POST.get('produto_preco_' + str(i))
            produto_subtotal = request.POST.get('produto_subtotal_' + str(i))
            print(f'produto_nome: {produto_nome}')
            print(f'produto_quantidade: {produto_quantidade}')
            print(f'produto_preco: {produto_preco}')
            print(f'produto_subtotal: {produto_subtotal}')

            item_compra = ItemBuy(
                buy=buy,
                produto=produto,
                quantidade=produto_quantidade,
                preco_unitario=produto_preco,
            )
            item_compra.save()

        # Função de predição sendo chamada de forma assíncrona
        def run_prediction():
            item_prediction = ItemPrediciton()
            asyncio.run(item_prediction.predict())  # Rodar a predição de forma assíncrona

        # Usar um executor de threads para rodar a predição em segundo plano        
        executor = ThreadPoolExecutor()
        executor.submit(run_prediction)     

        return redirect('bougth_finished')
    return redirect('cart')  



