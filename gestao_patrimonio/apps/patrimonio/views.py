from django.shortcuts import render
from apps.movimentacoes.models import Movimentacao
from .models import Bem, Categoria
from django.db import models

def dashboard(request):
    total_ativos = Bem.objects.count()
    valor_total_patrimonio = Bem.objects.aggregate(total=models.Sum("valor"))["total"] or 0
    ativos_manutencao = Bem.objects.filter(status="manutencao").count()
    
    categorias = Categoria.objects.all()
    categorias_labels = [c.nome for c in categorias]
    categorias_data = [Bem.objects.filter(categoria=c).count() for c in categorias]
    
    movimentacoes_recentes = Movimentacao.objects.order_by("-data")[:5]

    context = {
        "total_ativos": total_ativos,
        "valor_total_patrimonio": valor_total_patrimonio,
        "ativos_manutencao": ativos_manutencao,
        "categorias_labels": categorias_labels,
        "categorias_data": categorias_data,
        "movimentacoes_recentes": movimentacoes_recentes,
    }
    return render(request, "patrimonio/dashboard.html", context)