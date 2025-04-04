# Atributos de clase
class Pessoas: 

    # Os atributos de classe são declarados fora de um método diretamente na classe. 
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


# Podendo ser chamado diretamente
p1 = Pessoas.possui_olho
p2 = Pessoas.possui_orelha
p3 = Pessoas("Yhago", 18, "5348545345")

print(p1)
print(p2)
print("----")
print(p3.logar_sistema())