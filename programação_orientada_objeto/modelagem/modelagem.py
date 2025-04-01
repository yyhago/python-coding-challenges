class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f"{self.nome} está logando no sistema.")

p1 = Pessoas("Yhago", 18, "349342845424")
p2 = Pessoas("Henrique", 28, "58237346424")

p1.logar_sistema()
p2.logar_sistema()