from django.shortcuts import render
from .models import Produto


# Create your views here.
def index(requests):
    produto = Produto.objects.all()
    contexto = {
        'produtos': produto
    }

    return render(requests, 'index.html', contexto)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    contexto = {
        'produto_do_contexto': prod
    }
    return render(request, 'produto.html', contexto)
