from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField(max_length=9)
    descricao = models.TextField()
    def __str__(self):
        return self.nome

# Create your models here.
