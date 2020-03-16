class Autor:

    def __init__(self, primeiro_nome, ultimo_nome, nome_do_meio=''):
        self.primeiro_nome = primeiro_nome
        self.nome_do_meio = nome_do_meio
        self.ultimo_nome = ultimo_nome

    @property
    def nome_como_citado(self):
        primeira_letra_nome = self.primeiro_nome.upper()[0]
        return f'{self.ultimo_nome.upper()} {primeira_letra_nome}.'


    def __str__(self):
        return f'{self.primeiro_nome} {self.nome_do_meio} {self.ultimo_nome}'


class Livro:

    def __init__(self, titulo, ano, autores=None):
        if not autores:
            autores = []
        self.titulo = titulo
        self.ano = ano
        self.autores = autores


    @property
    def titulo(self):
        return self._titulo


    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError('Título é obrigatório')
        self._titulo = value


    def __str__(self):
        return self.titulo


class Biblioteca:

    def __init__(self, nome, livros=None):
        if not livros:
            livros = None
        self.nome = nome
        self.livros = livros


    @property
    def livros_por_autor(self):
        d_livros_por_autor = {}

        for livro in self.livros:
            for autor in livro.autores:
                if not d_livros_por_autor.get(autor.nome_como_citado):
                    d_livros_por_autor[autor.nome_como_citado] = []
                d_livros_por_autor[autor.nome_como_citado].append(livro.titulo)

        return d_livros_por_autor


    def __str__(self):
        return self.nome
