# Controller, controla a lógica da aplicação
from model import Pessoa
from dal import PessoaDal

class PessoaController:

    # Método responsável por verificar condições do input feito pelo usuário a ser cadastrado,
    # e posteriormente salvar na método da minha classe PessoaDal, com suas propriedades. 
    @classmethod
    def cadastrar(cls, nome: str, idade: int, altura: float, cpf: str):
        
        if len(nome) > 2 and idade > 10 and len(cpf) == 11:
            try:
                PessoaDal.salvar(Pessoa(nome, idade, altura, cpf))
                return True
            except:
                return False
            
    # Retorna os usuários percorridos no método listarUsuarios() da minha classe PessoaDal.
    @classmethod
    def listarUsuarios(cls):
        return PessoaDal.listarUsuarios()