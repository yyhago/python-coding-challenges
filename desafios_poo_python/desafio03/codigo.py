class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def cadastrar_livro(self, livro_cadastrado):
        self.livros.append(livro_cadastrado)

class Livro:
    def __init__(self, titulo, ano_publicacao, autor):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor = autor
        autor.livros.append(self) 

    def __repr__(self):
        return f"Livro: {self.titulo}"



autor = Autor("Robert Cecil Martin")
livro1 = Livro("Código Limpo", 2008, autor)
livro2 = Livro("Memórias Póstumas", 1881, autor)
print(autor.livros)
