while True:
    with open("meuTxt.txt", "a") as arquivo:

        adicionar_tarefa = int(input("1 - Adicionar Tarefa | 2 - Sair do programa: "))

        if adicionar_tarefa == 2:
            print("Encerrando...")
            break

        if adicionar_tarefa == 1:
            nova_tarefa = str(input("Insira sua tarefa: "))
            arquivo.write(nova_tarefa + "\n")  

            print("Tarefa adicionada com sucesso!")
            

            parar = int(input("Caso queira parar, digite 2. Caso contrário, digite 1 para continuar: "))
            if parar == 2:
                print("Encerrando...")
                break

print("Programa encerrado com sucesso!")
