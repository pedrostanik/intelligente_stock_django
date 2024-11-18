from django.db import models
from django.contrib.auth.models import User
import datetime

class Produtos(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=100)    
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    data_atualizacao = models.DateTimeField()
    imagem = models.ImageField(upload_to="fotos_produtos/%Y/%m/%d/", blank=True)    
    open_to_sell = models.BooleanField(default=False)
    def __str__(self):
        return self.nome
    
class ItemBuy(models.Model):
    buy = models.ForeignKey('Buy', on_delete=models.CASCADE)  # Relacionamento com a tabela de compras
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'buy={self.buy}, produto={self.produto}, quantidade={self.quantidade}, preco_Unitario={self.preco_unitario}' 

class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_sell = models.DateTimeField(auto_now_add=True)
    week_day = models.CharField(max_length=10) 
    month_day = models.PositiveSmallIntegerField()
    weakend = models.BooleanField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'buy={self.user}, produto={self.date_sell}, quantidade={self.week_day}, preco_Unitario={self.month_day}, preco_Unitario={self.weakend}, preco_Unitario={self.total}' 

    

