# Atributos de instancia
class Pessoas: 
    def __init__(self, nome, idade, cpf):
        self.nome = nome # O "self" é usado para armazenar os valores na instância
        self.idade = idade
        self.cpf = cpf

    def retornar_dados(self): # Sempre que acessamos atributos da instância dentro de um método, usamos 'self'
        return self.nome, self.idade, self.cpf

    def logar_sistema(self):
        print(f"Dados: {self.retornar_dados()}") # Chamando outro método da classe


p1 = Pessoas("Yhago", 18, "342423456") 
p1.logar_sistema()