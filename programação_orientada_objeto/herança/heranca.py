class Pessoa: # Classe "Pessoa" que tem métodos que uma pessoa tem

    def falar(self):
        print("Estou falando!")

    def andar(self):
        print("Estou andando!")

class Vendedor(Pessoa): # Classe "Vendedor" com herança da classe "Pessoa", podendo acessar tudo de lá (atributos ou métodos)
    
    def vendendo(self):
        print("Estou vendendo!")
    
class Cliente(Pessoa): # Classe "Cliente" com herança da classe "Pessoa", podendo acessar tudo de lá (atributos ou métodos)

    def comprar(self):
        print("Estou comprando")


# Instancia do vendedor e cliente e chamando seus métodos

v1 = Vendedor()
v1.falar()
v1.andar()
v1.vendendo()

print("----")

c1 = Cliente()
c1.falar()
c1.andar()
c1.comprar()
