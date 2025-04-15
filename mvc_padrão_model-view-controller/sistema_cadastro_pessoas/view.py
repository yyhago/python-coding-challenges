# View, responsável pela visualização/interface do usuário
from controller import PessoaController

while True:

    opcaoUsuario = int(input("1 <- Adicionar Usuário | 2 <- Sair"))

    if opcaoUsuario == 2:
        print("Encerrando sistema..")
        break

    elif opcaoUsuario == 1:
        nome = str(input("Nome do usuário: "))
        idade = int(input("Idade do usuário: "))
        altura = float(input("Altura do usuário: "))
        cpf = str(input("CPF do usuário: "))
        if PessoaController.cadastrar(nome, idade, altura, cpf):
            print("Usuário cadastrado com sucesso")
        else:
            print("ERRO!\n Digite os valores corretamente.")