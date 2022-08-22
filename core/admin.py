from django.contrib import admin

from .models import produto, cliente
class produtoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque')


class clientedados(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')

admin.site.register(produto, produtoAdmin)
admin.site.register(cliente, clientedados)
