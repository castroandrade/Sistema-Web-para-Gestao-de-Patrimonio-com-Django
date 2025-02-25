from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name="Nome do Departamento")
    responsavel = models.CharField(max_length=255, verbose_name="Responsável")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"