# Dal, camada que lê/grava no "banco"
from model import Pessoa

class PessoaDal:

    # Criação do método salvar usando o "@classmethod" pois pega as propriedades da própria classe e retorna em um txt com as informações
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoas.txt", "w") as arquivo:
            arquivo.write(f"Nome: {pessoa.nome} | Idade:{pessoa.idade}\n Altura: {pessoa.altura} | CPF: {pessoa.cpf}")


    # @classmethod
    # def ler(cls):
    #     nome = "Yhago"
    #     idade = 18
    #     altura = 1.67
    #     cpf = "1602934804"
    #     return Pessoa(nome, idade, altura, cpf)