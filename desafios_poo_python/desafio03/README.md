3. Sistema de Livros e Autores 
Crie as classes Autor e Livro com relacionamento bidirecional.
Regras:

Autor tem nome e livros (lista de livros).
Livro tem titulo, ano_publicacao e autor.
Ao associar um livro a um autor, atualize a lista livros automaticamente.

Exemplo:
autor = Autor("Machado de Assis")
livro1 = Livro("Dom Casmurro", 1899, autor)
livro2 = Livro("Memórias Póstumas", 1881, autor)
print(autor.livros)  # [Livro: Dom Casmurro, Livro: Memórias Póstumas]