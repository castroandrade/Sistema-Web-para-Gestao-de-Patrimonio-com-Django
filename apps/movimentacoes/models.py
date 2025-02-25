from django.db import models
from apps.patrimonio.models import Bem
from apps.departamentos.models import Departamento

class Movimentacao(models.Model):
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE, verbose_name="Bem Movimentado")
    origem = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True, related_name="movimentacoes_origem", verbose_name="Departamento de Origem")
    destino = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True, related_name="movimentacoes_destino", verbose_name="Departamento de Destino")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da Movimentação")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição da Movimentação")

    def __str__(self):
        return f"{self.bem} movimentado em {self.data.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        verbose_name = "Movimentação de Bem"
        verbose_name_plural = "Movimentações de Bens"

class HistoricoStatus(models.Model):
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE, verbose_name="Bem")
    status_anterior = models.CharField(max_length=50, verbose_name="Status Anterior")
    status_atual = models.CharField(max_length=50, verbose_name="Status Atual")
    alterado_por = models.CharField(max_length=255, verbose_name="Usuário que Alterou")
    data_alteracao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Alteração")

    def __str__(self):
        return f"{self.bem} mudou de {self.status_anterior} para {self.status_atual}"

    class Meta:
        verbose_name = "Histórico de Status"
        verbose_name_plural = "Histórico de Status"