from django.test import TestCase
from django.urls import reverse
from apps.patrimonio.models import Bem, Categoria
from datetime import date
from django.contrib.auth.models import User

class PatrimonioViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="Test@123456")
        self.client.login(username="admin", password="Test@123456")
        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.bem = Bem.objects.create(
            nome="Notebook",
            identificador_rfid="RFID-1234",
            categoria=self.categoria,
            status="ativo",
            valor=3000.00,
            data_aquisicao=date.today(),
        )

    def test_listagem_bens(self):
        """Testa se a página de listagem de bens carrega corretamente"""
        response = self.client.get(reverse("patrimonio:lista_bens"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "patrimonio/lista.html")
