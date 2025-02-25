from django.shortcuts import render
from .models import Movimentacao, HistoricoStatus

def lista_movimentacoes(request):
    """ Lista todas as movimentações de bens """
    movimentacoes = Movimentacao.objects.order_by("-data")
    return render(request, "movimentacoes/lista.html", {"movimentacoes": movimentacoes})

def lista_historico_status(request):
    """ Lista todas as mudanças de status dos bens """
    historico_status = HistoricoStatus.objects.order_by("-data_alteracao")
    return render(request, "movimentacoes/historico_status.html", {"historico_status": historico_status})
