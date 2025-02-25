from django.test import TestCase
from apps.patrimonio.models import Bem, Categoria

class PatrimonioModelsTest(TestCase):
    def test_criacao_categoria(self):
        """Teste de criação de uma categoria de bem"""
        categoria = Categoria.objects.create(nome="Móveis")
        self.assertEqual(str(categoria), "Móveis")
