from django.contrib import admin
from .models import Produtos

class ProdutosAdmin(admin.ModelAdmin):
    list_display= ('id', 'nome', 'preco', 'quantidade', 'open_to_sell')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_editable = ('open_to_sell',)
    list_per_page = 10


admin.site.register(Produtos, ProdutosAdmin)

# Register your models here.
