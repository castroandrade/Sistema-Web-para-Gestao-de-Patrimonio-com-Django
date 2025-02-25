from django.test import TestCase
from django.contrib.auth.models import User

class TestUsuariosModelsTest(TestCase):
    def test_criacao_usuario(self):
        """Teste de criação de um usuário Django padrão"""
        user = User.objects.create_user(username="testuser", password="Test@123456")
        self.assertEqual(user.username, "testuser")
