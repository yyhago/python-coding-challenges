2. Classe Retângulo com Propriedades

Crie uma classe Retangulo com atributos privados e validações.
Requisitos:

Atributos privados __largura e __altura.
Propriedades (@property e @setter) para validar valores positivos.
Métodos area() e eh_quadrado().

Exemplo:
ret = Retangulo(5, 3)
print(ret.area())         # 15
print(ret.eh_quadrado())  # False
ret.largura = 3
print(ret.eh_quadrado())  # True