from django.shortcuts import render
from apps.patrimonio.models import Bem, Categoria
from apps.movimentacoes.models import Movimentacao
from django.db.models import Count, Sum

def home(request):
    return render(request, "base.html")

def dashboard(request):
    """Exibe o dashboard com métricas do sistema"""
    total_bens = Bem.objects.count()
    valor_total_patrimonio = Bem.objects.aggregate(Sum("valor"))["valor__sum"] or 0

    # Distribuição por categoria
    categorias = Categoria.objects.all()
    categorias_labels = [c.nome for c in categorias]
    categorias_data = [Bem.objects.filter(categoria=c).count() for c in categorias]

    # Status de manutenção
    status_labels = ["Ativo", "Baixado", "Em Manutenção"]
    status_data = [
        Bem.objects.filter(status="ativo").count(),
        Bem.objects.filter(status="baixado").count(),
        Bem.objects.filter(status="manutencao").count(),
    ]

    # Últimas movimentações
    movimentacoes_recentes = Movimentacao.objects.order_by("-data")[:5]

    context = {
        "total_bens": total_bens,
        "valor_total_patrimonio": valor_total_patrimonio,
        "categorias_labels": categorias_labels,
        "categorias_data": categorias_data,
        "status_labels": status_labels,
        "status_data": status_data,
        "movimentacoes_recentes": movimentacoes_recentes,
    }
    return render(request, "dashboard.html", context)
