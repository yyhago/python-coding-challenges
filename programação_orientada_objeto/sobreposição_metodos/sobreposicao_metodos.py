class InfoPessoas: # Criamos a classe PAI com seus atributos
    def __init__(self, nome, idade, rg):
        self.nome = nome
        self.idade = idade
        self.rg = rg

    def exibir_info(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | RG: {self.rg}")

class Vendedor(InfoPessoas): # Criamos a classe filho com herança da classe PAI, pegando os valores e retradando sem duplicar com "super()"
    def __init__(self, id_vendedor, nome, idade, rg):
        super().__init__(nome, idade, rg)
        self.id_vendedor = id_vendedor

    def exibir_info(self):
        return f"Vendedor: {self.nome} | ID: ({self.id_vendedor}) | Idade: {self.idade} | RG: {self.rg}"

class Cliente(InfoPessoas): # Criamos a classe filho com herança da classe PAI, pegando os valores e retradando sem duplicar com "super()"
    def __init__(self, id_cliente, nome, idade, rg):
        super().__init__(nome, idade, rg)
        self.id_cliente = id_cliente

    def exibir_info(self):
        return f"Cliente: {self.nome} | ID: ({self.id_cliente}) | Idade: {self.idade} | RG: {self.rg}"

# Output de saída instanciando as minhas classes
v1 = Vendedor(1,"Yhago",18,"5483534")
c1 = Cliente(4, "Felipe", 45, "4585934053")
print(v1.exibir_info())
print(c1.exibir_info())