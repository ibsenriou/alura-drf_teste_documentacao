from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo='Procurando ninguém em latim',
            tipo='F',
            data_lancamento='2003-07-04',
            likes=2340,
            dislikes=40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo Serializados"""
        data = self.serializer.data
        self.assertEquals(set(data.keys()), {'titulo', 'tipo', 'data_lancamento', 'likes'})

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o CONTEÚDO dos campos que estão sendo Serializados"""
        data = self.serializer.data
        self.assertEquals(data['titulo'], self.programa.titulo)
        self.assertEquals(data['tipo'], self.programa.tipo)
        self.assertEquals(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEquals(data['likes'], self.programa.likes)


