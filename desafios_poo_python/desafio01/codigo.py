class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.valor = valor
        self.saldo += valor
        print(f"Foi adicionado R$ {valor}, em sua conta. O valor total deu {self.saldo}")

    def sacar(self, valor):
        self.valor = valor
        self.saldo -= valor
        print(f"Foi removido R$ {self.valor}, em sua conta.")
        print(f"O valor atual em sua conta é de R$ {self.saldo}")

    def __str__(self):
        return (f"Titular: {self.titular} | Saldo: R$ {self.saldo}")


titular = str(input("Digite seu nome:"))
saldo = 0

print(f"Olá {titular}, seja bem vindo!")
c1 = ContaBancaria(titular,saldo)

while True:
    print(f"Saldo R$ {c1.saldo}")
    opcao = int(input("1 - Depositar | 2 - Sacar | 3 - Sair: "))

    if opcao == 1:
        valor = float(input("Digite o valor que deseja depositar: "))
        c1.depositar(valor)

    if opcao == 2:
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor > c1.saldo:
            print("Você não tem saldo suficiente para este saque!")
        else:
            c1.sacar(valor)
    
    if opcao == 3:
        print("Encerrou!")
        print(f"Titular: {titular} | Saldo: R$ {c1.saldo}")
        break
