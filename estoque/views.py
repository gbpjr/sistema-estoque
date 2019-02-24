from django.shortcuts import render, redirect
from .models import Local, Tipo, Fabricante, Componente, Log
from estoque.forms import ComponenteForm
from django.http import Http404, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import json


def index(request, componentes=''):
    locais = Local.objects.all()
    tipos = Tipo.objects.all()
    fabricantes = Fabricante.objects.all()
    componentes = Componente.objects.all()
    return render(request, 'estoque/index.html', {'componentes': componentes, 'fabricantes': fabricantes, 'tipos': tipos, 'locais': locais})

@login_required()
def filtrar(request):
    filters = {}
    tipo = request.GET.get('tipo')
    if tipo:
        tipo = Tipo.objects.get(nome=tipo)
        filters['tipo'] = tipo
    fabricante = request.GET.get('fabricante')
    if fabricante:
        fabricante = Fabricante.objects.get(nome=fabricante)
        filters['fabricante'] = fabricante
    local = request.GET.get('local')
    if local:
        local = Local.objects.get(nome=local)
        filters['local'] = local
    query = request.GET.get('query')
    if query:
        componentes = Componente.objects.filter(**filters).filter(nome__startswith = query)
    else:
        componentes = Componente.objects.filter(**filters)

    locais = Local.objects.all()
    tipos = Tipo.objects.all()
    fabricantes = Fabricante.objects.all()

    return render(request, 'estoque/index.html', {'componentes': componentes, 'locais': locais, 'tipos': tipos, 'fabricantes': fabricantes})

@login_required
def remover(request, componente_id):
    if request.method == 'POST':
        componente = Componente.objects.get(id=componente_id)
        quantidade = request.POST.get('quantidade')
        quantidade = int(quantidade)
        if validar_remocao(componente.quantidade, quantidade):
            componente.quantidade-=quantidade
            componente.save()
            log = Log()
            log.usuario = request.user
            log.componente = componente
            log.quantidade = quantidade
            log.horario = timezone.now()
            log.save()

            data = serializers.serialize("json", Log.objects.all())

            with open('estoque/logs/logs.json','w') as f:
                json.dump(data, f)


            return redirect('../../')
        else:
            mensagem = "A quantia é superior à disponível. Tente novamente."
            return render(request, 'estoque/remover.html', {'componente': componente, 'mensagem': mensagem})
    else:
        componente = Componente.objects.get(id=componente_id)
        return render(request, 'estoque/remover.html', {'componente': componente})


def validar_remocao(qtde_total, qtde_retirada):
    if qtde_retirada > qtde_total:
        return False
    else:
        return True

@login_required
def pdf(request):
    return render(request, 'estoque/pdf.html', {})
