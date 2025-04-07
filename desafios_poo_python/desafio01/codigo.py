class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        saldo = 0

    def depositar(self, valor):
        self.valor = valor
        self.saldo += valor
        print(f"Foi adicionado R$ {valor}, em sua conta. O valor total deu {self.saldo}")

    def sacar(self, valor):
        self.valor = valor
        self.saldo -= valor
        print(f"Foi removido R$ {self.valor}, em sua conta.")

    def __str__(self):
        return (f"Titular: {self.titular} | Saldo: R$ {self.saldo}")

c1 = ContaBancaria("Yhago", 100)
print(c1)
c1.depositar(50)
c1.sacar(30)
print(c1)