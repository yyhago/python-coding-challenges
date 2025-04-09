class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, valor):
        self.itens.append(valor)

    def pop(self):
        if not self.itens:
            raise ValueError("Pilha vazia")
        return self.itens.pop()

    def topo(self):
        if not self.itens:
            raise ValueError("Pilha vazia")
        return self.itens[-1]

    def __len__(self):
        return len(self.itens)

    def __eq__(self, outra):
        if not isinstance(outra, Pilha):
            return False
        return self.itens == outra.itens

    def __ne__(self, outra):
        return not self.__eq__(outra)


p1 = Pilha()
p1.push(1)
p1.push(2)
p1.push(3)
print(p1.topo())     # 3
print(len(p1))       # 3

p2 = Pilha()
p2.push(1)
p2.push(2)
p2.push(3)
print(p1 == p2)      # True
