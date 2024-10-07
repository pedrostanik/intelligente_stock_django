from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)    
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    data_atualizacao = models.DateTimeField()
    # image = models.ImageField(upload_to='produtos/', blank=True, null=True)
    imagem = models.CharField(max_length=100, default='none',)


    
    def __str__(self):
        return self.nome

# Create your models here.
