import os
import sys
import django
import pandas as pd
import asyncio
from surprise import Reader, Dataset, SVD

# Adicionar o caminho do projeto ao sys.path
# Supondo que o diretório do projeto esteja um nível acima do diretório onde o script está localizado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Definir a variável de ambiente DJANGO_SETTINGS_MODULE
# Aqui você deve usar o nome do seu projeto Django. Exemplo: 'meu_projeto.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

# Inicializar o Django
django.setup()

from produtos.models import Buy, ItemBuy
from django.contrib.auth.models import User

class ItemPrediciton():
    def __init__(self):
        self.buys = pd.DataFrame(Buy.objects.all().values())
        self.itens_buy = pd.DataFrame(ItemBuy.objects.all().values())
        self.users = pd.DataFrame(User.objects.all().values())

    async def predict(self):
        await asyncio.sleep(20)
        print(self.buys)
        print(self.itens_buy)
        print(self.users)        

        # Unir as tabelas
        df = pd.merge(self.buys, self.itens_buy, left_on='id', right_on='buy_id')

        #Matriz contagens
        matriz_contagens = pd.pivot_table(df, values='quantidade', index='user_id', columns='produto_id', aggfunc='sum')
        print(f'matriz_contagens: {matriz_contagens}')

        # Criar um leitor com um intervalo de ratings que represente as contagens
        reader = Reader(rating_scale=(0, df.max().max()))
        # Carregar os dados para o Surprise
        data = Dataset.load_from_df(df.stack().reset_index(name='count'), reader)


        # Criar a matriz de ratings (simplificado, considerando quantidade como rating)
        # reader = Reader(rating_scale=(1, df['quantidade'].max()))
        # data = Dataset.load_from_df(df[['user_id', 'produto_id', 'quantidade']], reader)

        # Criar o modelo (SVD é um algoritmo popular)
        trainset = data.build_full_trainset()
        algo = SVD()
        algo.fit(trainset)

        # Fazer uma predição para um usuário específico e um produto
        uid = '1'  # ID do usuário
        iid = '10'  # ID do produto
        print('Predicting!')
        pred = algo.predict(uid, iid, r_ui=4, verbose=True)
        
        print(f'pred: {pred}')


if __name__ == '__main__':
    item_prediction = ItemPrediciton()
    item_prediction.predict()