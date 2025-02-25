from django.test import TestCase
from django.urls import reverse
from apps.departamentos.models import Departamento
from django.contrib.auth.models import User

class DepartamentosViewsTest(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(nome="Financeiro", responsavel="João")
        self.user = User.objects.create_user(username="admin", password="Test@123456")
        self.client.login(username="admin", password="Test@123456")

    def test_listagem_departamentos(self):
        """Testa se a página de listagem de departamentos carrega corretamente"""
        response = self.client.get(reverse("departamentos:lista_departamentos"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "departamentos/lista.html")
