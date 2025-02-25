from django.urls import path
from .views import lista_movimentacoes, lista_historico_status

app_name = "movimentacoes"

urlpatterns = [
    path("", lista_movimentacoes, name="lista_movimentacoes"),
    path("historico-status/", lista_historico_status, name="lista_historico_status"),
]
