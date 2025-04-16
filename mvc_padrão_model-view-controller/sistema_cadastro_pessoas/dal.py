# Dal, camada que lê/grava no "banco"
from model import Pessoa

class PessoaDal:

    # Salva os dados de uma pessoa (nome, idade, altura e CPF) no arquivo "pessoas.txt", 
    # sobrescrevendo o conteúdo anterior. Os dados são separados por vírgula para facilitar a leitura posterior.
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoas.txt", "a") as arquivo:
            arquivo.write(f"{pessoa.nome},{pessoa.idade},{pessoa.altura},{pessoa.cpf}\n")


    # Lê o arquivo "pessoas.txt", separa os dados de cada linha (nome, idade, altura e cpf),
    # cria objetos da classe Pessoa com essas informações e os adiciona em uma lista.
    # Retorna a lista contendo todos os usuários cadastrados.
    @classmethod
    def listarUsuarios(cls):
        lista_armazenada_usuarios = []

        try:
            with open("pessoas.txt", "r") as arquivo:
                linhas = arquivo.readlines()

                for linha in linhas:
                    dados = linha.strip().split(",")

                    if len(dados) == 4:
                        try:
                            nome = dados[0]
                            idade = int(dados[1])
                            altura = float(dados[2])
                            cpf = dados[3]

                            pessoa = Pessoa(nome, idade, altura, cpf)
                            lista_armazenada_usuarios.append(pessoa)

                        except ValueError:
                            print(f"Atenção: Dado errado na linha! -> {linha.strip()}.")

        except FileNotFoundError:
            print("Erro: 'pessoas.txt' arquivo não existente.")

        return lista_armazenada_usuarios