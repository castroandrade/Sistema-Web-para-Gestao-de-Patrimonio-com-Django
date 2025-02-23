from django.db import models
from apps.fornecedores.models import Fornecedor
from apps.departamentos.models import Departamento

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name="Nome da Categoria")
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Bem(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Bem")
    identificador_rfid = models.CharField(max_length=50, unique=True, verbose_name="Etiqueta RFID")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fornecedor")
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Departamento Atual")
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor do Bem", null=True, blank=True)
    status = models.CharField(max_length=50, choices=[("ativo", "Ativo"), ("baixado", "Baixado"), ("manutencao", "Em Manutenção")], default="ativo")

    def __str__(self):
        return f"{self.nome} ({self.identificador_rfid})"

    class Meta:
        verbose_name = "Bem Patrimonial"
        verbose_name_plural = "Bens Patrimoniais"