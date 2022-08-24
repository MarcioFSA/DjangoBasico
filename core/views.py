from django.shortcuts import render
from .models import produto
# Create your views here.

def index(request):
    produtos = produto.objects.all()
    print(produtos)
    context = {
        'Curso': 'Django Web',
        'outro':'O Django é massa',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def Produto(request, pk):
    Prod = produto.objects.get(id=pk)
    context ={
        'produto': Prod
    }
    return render(request, 'produto.html', context)
