# Métodos de classe
class Pessoas: 

    possui_olho = True
    possui_orelha = False

    def __init__(self, nome, idade, cpf):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf

    def retornar_dados(self): 
        return self.nome, self.idade, self.cpf

    def logar_sistema(self):
        print(f"Dados: {self.retornar_dados()}")

    # Um método de classe permite você criar um método sem ter que instancialo em sua instancia
    @classmethod # O "@classmethod" juntamente com (cls) indica que esse método faz parte da classe e é um método de classe
    def programar(cls,linguagem): 
        print(f"O programador está programando em {linguagem} no momento")


# p1 = Pessoas.possui_olho
# p2 = Pessoas.possui_orelha
# p3 = Pessoas("Yhago", 18, "5348545345")

# Chamando a classe e seu método diretamente!
Pessoas.programar("Python")

