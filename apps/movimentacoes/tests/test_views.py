from django.test import TestCase
from django.urls import reverse
from apps.movimentacoes.models import Movimentacao
from apps.patrimonio.models import Bem, Categoria
from apps.departamentos.models import Departamento
from datetime import date
from django.contrib.auth.models import User

class MovimentacoesViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="Test@123456")
        self.client.login(username="admin", password="Test@123456")

        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.departamento_origem = Departamento.objects.create(nome="TI", responsavel="Gestor TI")
        self.departamento_destino = Departamento.objects.create(nome="RH", responsavel="Gestor RH")
        self.bem = Bem.objects.create(
            nome="Notebook",
            identificador_rfid="RFID-5678",
            categoria=self.categoria,
            status="ativo",
            valor=5000.00,
            data_aquisicao=date.today(),
        )
        self.movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            origem=self.departamento_origem,
            destino=self.departamento_destino
        )

    def test_listagem_movimentacoes(self):
        """Testa se a página de listagem de movimentações carrega corretamente"""
        response = self.client.get(reverse("movimentacoes:lista_movimentacoes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movimentacoes/lista.html")
