class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property # O 'property' le os valores
    def largura(self):
        return self.__largura
    
    @largura.setter # modifica os valores
    def largura(self,valor):
        if valor <= 0:
            raise ValueError("A largura deve ser positiva")
        self.__largura = valor
    
    @property # O 'property' le os valores
    def altura(self):
        return self.__altura
    
    @altura.setter # modifica os valores
    def altura(self,valor):
        if valor <= 0:
            raise ValueError("A altura deve ser positiva")
        self.__altura = valor

    # métodos para calcular area e ver se é quadrado
    def area(self):
        return self.__largura * self.__altura
    
    def eh_quadrado(self):
        return self.__largura == self.__altura
    

reta = Retangulo(5,3)
print(reta.area())

print(reta.eh_quadrado())

reta2 = Retangulo(3,3)
print(reta2.eh_quadrado())