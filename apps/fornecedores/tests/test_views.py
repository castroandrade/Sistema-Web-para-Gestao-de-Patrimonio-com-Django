from django.test import TestCase
from django.urls import reverse
from apps.fornecedores.models import Fornecedor
from django.contrib.auth.models import User

class FornecedoresViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="Test@123456")
        self.client.login(username="admin", password="Test@123456")
        self.fornecedor = Fornecedor.objects.create(
            nome="Tech Solutions",
            cnpj="12.345.678/0001-90",
            telefone="(11) 99999-9999",
            email="contato@techsolutions.com"
        )

    def test_listagem_fornecedores(self):
        """Testa se a página de listagem de fornecedores carrega corretamente"""
        response = self.client.get(reverse("fornecedores:lista_fornecedores"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "fornecedores/lista.html")
