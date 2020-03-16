import unittest
from funcs import maior, soma, media, valores_iguais, indice_prim_valor_igual
from models import Autor, Livro, Biblioteca


class MaiorTestCase(unittest.TestCase):

    def test_a_maior_b(self):
        A = 2
        B = 1
        self.assertEqual(maior(A, B), A)

    def test_b_maior_a(self):
        A = 1
        B = 2
        self.assertEqual(maior(A, B), B)

    def test_a_igual_b(self):
        A = 1
        B = 1
        self.assertEqual(maior(A, B), A)
        self.assertEqual(maior(A, B), B)


class SomaTestCase(unittest.TestCase):

    def test_soma_lista(self):
        lista = [1, 2, 3, 4]
        self.assertEqual(soma(lista), 10)

    def test_soma_lista_vazia(self):
        lista = []
        self.assertEqual(soma(lista), 0)

    def test_soma_lista_elemento_opcional(self):
        lista = [1, 2, 3, 4]
        self.assertEqual(soma(lista, 2), 12)


class MediaTestCase(unittest.TestCase):

    def test_media_lista(self):
        lista = [1, 2, 3, 4, 0]
        self.assertEqual(media(lista), 2)

    def test_media_lista_vazia(self):
        lista = []
        self.assertEqual(media(lista), 0)


class ValoresIguaisTestCase(unittest.TestCase):

    def test_valores_iguais_lista(self):
        lista1 = [1, 2, 3, 4, 0]
        lista2 = [2, 3, 9, 10, 85, 1]
        self.assertEqual(valores_iguais(lista1, lista2), [1, 2, 3])

    def test_valores_iguais_valores_diferentes(self):
        lista1 = [1, 2, 3, 4, 0]
        lista2 = [99, 100, 50, 22]
        self.assertEqual(valores_iguais(lista1, lista2), [])


class IndicePrimValorIgual(unittest.TestCase):
    def test_indice_prim_valor_igual_lista(self):
        lista1 = [1, 2, 3, 4, 0]
        lista2 = [2, 3, 9, 10, 85, 1]
        self.assertEqual(indice_prim_valor_igual(lista1, lista2), 0)

    def test_indice_prim_valor_igual_valores_diferentes(self):
        lista1 = [1, 2, 3, 4, 0]
        lista2 = [99, 100, 50, 22]
        self.assertIsNone(indice_prim_valor_igual(lista1, lista2))


class AutorModelTestCase(unittest.TestCase):

    def test_autor_sem_nome_do_meio(self):
        autor = Autor(primeiro_nome='Machado', ultimo_nome='Assis')
        self.assertEqual(autor.primeiro_nome, 'Machado')
        self.assertEqual(autor.nome_do_meio, '')
        self.assertEqual(autor.ultimo_nome, 'Assis')


    def test_autor_com_nome_do_meio(self):
        autor = Autor(
            primeiro_nome='Carlos', ultimo_nome='Andrade', nome_do_meio='Drummond')
        self.assertEqual(autor.primeiro_nome, 'Carlos')
        self.assertEqual(autor.nome_do_meio, 'Drummond')
        self.assertEqual(autor.ultimo_nome, 'Andrade')


    def test_nome_como_citado(self):
        autor = Autor(
            primeiro_nome='carlos', ultimo_nome='andrade', nome_do_meio='drummond')
        self.assertEqual(autor.nome_como_citado, 'ANDRADE C.')


class LivroModelTestCase(unittest.TestCase):

    def test_titulo_obrigatorio(self):
        with self.assertRaises(ValueError):
            Livro(titulo='', ano=2020)


class BibliotecaModelTestCase(unittest.TestCase):

    def setUp(self):
        self.autores = [
            Autor(primeiro_nome='Carlos', ultimo_nome='Andrade', nome_do_meio='Drummond'),
            Autor(primeiro_nome='Machado', ultimo_nome='Assis')
        ]

        self.livros = [
            Livro(titulo='DOM CASMURRO', ano=1899, autores=[self.autores[0]]),
            Livro(titulo='QUINCAS BORBA', ano=1891, autores=[self.autores[0]]),
            Livro(titulo='ALGUMA POESIA', ano=1930, autores=[self.autores[1]]),
            Livro(titulo='CLARO ENIGMA', ano=1951, autores=[self.autores[1]]),
        ]


    def test_livros_por_autor(self):
        biblioteca = Biblioteca(
            nome='Biblioteca Pública de Belo Horizonte', livros=self.livros)
        self.assertDictEqual(
            biblioteca.livros_por_autor,
            {
                'ANDRADE C.': ['DOM CASMURRO', 'QUINCAS BORBA'],
                'ASSIS M.': ['ALGUMA POESIA', 'CLARO ENIGMA']
            }
        )

if __name__ == '__main__':
    unittest.main()
