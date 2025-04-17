# View, responsável pela visualização/interface do usuário
from controller import PessoaController

# Interface gráfica em terminal para o usuário!
while True:
    opcaoUsuario = int(input(
        "1 <- Adicionar Usuário | 2 <- Listar Usuários | 3 <- Buscar por CPF | 4 <- Excluir por CPF | 9 <- Sair\n"
    ))

    if opcaoUsuario == 9:
        print("Encerrando sistema..")
        break

    elif opcaoUsuario == 1:
        nome = str(input("Nome do usuário: "))
        idade = int(input("Idade do usuário: "))
        altura = float(input("Altura do usuário: "))
        cpf = str(input("CPF do usuário: "))

        if PessoaController.cadastrar(nome, idade, altura, cpf):
            print("Usuário cadastrado com sucesso.")
        else:
            print("ERRO!\nDigite os valores corretamente.")

    elif opcaoUsuario == 2:
        lista = PessoaController.listarUsuarios()

        if lista:
            print("Lista de usuários:")
            for pessoa in lista:
                print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Altura: {pessoa.altura}, CPF: {pessoa.cpf}")
        else:
            print("ERRO! Não há usuários cadastrados ou houve um erro ao listar.")

    elif opcaoUsuario == 3:
        cpf_procurado = str(input("Digite o CPF a ser buscado: "))
        pessoa = PessoaController.buscaCPF(cpf_procurado)

        if pessoa:
            print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Altura: {pessoa.altura}, CPF: {pessoa.cpf}")
        else:
            print("ERRO! CPF não encontrado ou houve um erro ao buscar.")

    elif opcaoUsuario == 4:
        cpf = str(input("Digite o CPF a ser excluído: "))

        if PessoaController.deletarUsuario(cpf):
            print("Usuário excluído com sucesso.")
        else:
            print("ERRO! CPF não encontrado ou houve um erro ao excluir.")
