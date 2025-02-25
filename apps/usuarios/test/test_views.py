from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestUsuariosViewsTest(TestCase):
    def test_acesso_a_pagina_de_registro(self):
        """Teste se a página de registro carrega corretamente"""
        response = self.client.get(reverse("usuarios:registro"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "usuarios/registro.html")

    def test_registro_de_usuario(self):
        """Teste se um usuário pode se registrar"""
        response = self.client.post(reverse("usuarios:registro"), {
            "username": "testuser",
            "password1": "Test@123456",
            "password2": "Test@123456"
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após sucesso
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_login_usuario(self):
        """Teste de login com usuário válido"""
        User.objects.create_user(username="testuser", password="Test@123456")
        response = self.client.post(reverse("usuarios:login"), {
            "username": "testuser",
            "password": "Test@123456"
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para dashboard
