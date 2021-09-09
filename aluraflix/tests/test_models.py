from django.test import TestCase
from aluraflix.models import Programa


class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='Procurando ninguém em latim',
            data_lancamento='2003-07-04'
        )

    def test_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos de um Programa com valores default"""
        self.assertEquals(self.programa.titulo, 'Procurando ninguém em latim')
        self.assertEquals(self.programa.tipo, 'F')
        self.assertEquals(self.programa.data_lancamento, '2003-07-04')
        self.assertEquals(self.programa.likes, 0)
        self.assertEquals(self.programa.dislikes, 0)
