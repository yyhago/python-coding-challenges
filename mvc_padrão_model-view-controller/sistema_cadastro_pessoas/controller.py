# Controller, controla a lógica da aplicação
from model import Pessoa
from dal import PessoaDal

class PessoaController:

    @classmethod
    def cadastrar(cls, nome: str, idade: int, altura: float, cpf: str):
        
        if len(nome) > 2 and idade > 10 and len(cpf) == 11:
            try:
                PessoaDal.salvar(Pessoa(nome, idade, altura, cpf))
                return True
            except:
                return False