1. Classe Conta Bancária

Crie uma classe ContaBancaria que simule uma conta bancária simples.
Métodos:

__init__(self, titular: str, saldo: float = 0): Inicializa a conta.
depositar(self, valor: float): Adiciona um valor ao saldo.
sacar(self, valor: float): Subtrai um valor do saldo (se houver saldo suficiente).
__str__(self): Retorna uma string formatada com titular e saldo.

Exemplo:
conta = ContaBancaria("João", 100)
conta.depositar(50)
conta.sacar(30)
print(conta)  # Saída: Titular: João | Saldo: R$120.00