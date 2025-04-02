# Classe com Construtor (__init__)
class Pessoas: 
    def __init__(self, nome, idade): # A função __init__ é chamada automaticamente quando uma nova instancia da classe é criada, e serve para inicializar os atributos do projeto.
        print(f"{nome} | {idade}") # Podesse passar os valores diretamente, sem o self

    def logar_sistema(self): 
        print(f"Estou logando no sistema.")

# Criando uma instância da classe Pessoas
p1 = Pessoas("Yhago", 18) # Chama automaticamente o __init__
p1.logar_sistema() # Chamando o método logar_sistema()