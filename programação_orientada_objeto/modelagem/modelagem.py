class Pessoas: # Criação da classe Pessoas e passando seus atributos (caracteristicas)
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self): # Criação do método "logar_sistema()" que passa uma mensagem pegando o nome da pessoa pelo "self.nome"
        print(f"{self.nome} está logando no sistema.")

# Instanciando duas pessoas com a classe Pessoas onde passo os valores de seus atributos
p1 = Pessoas("Yhago", 18, "349342845424")
p2 = Pessoas("Henrique", 28, "58237346424")

# Chama o método "logar_sistema()" para cada instancia
p1.logar_sistema()
p2.logar_sistema()