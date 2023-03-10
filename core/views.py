from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto

from django.http import HttpResponse
from django.template import loader


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
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    
    contexto = {
        'produto_do_contexto': prod
    }
    return render(request, 'produto.html', contexto)


def error404(request, ex):
    template  = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template  = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
