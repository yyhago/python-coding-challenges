4. Pilha Personalizada

Implemente uma classe Pilha com operações LIFO.
Métodos:

push(valor): Adiciona ao topo.
pop(): Remove e retorna o topo (ou lança ValueError se vazia).
topo(): Retorna o topo sem remover.
__len__(): Retorna o tamanho.
Bônus: Suporte a comparações (==, !=).

Exemplo:
p1 = Pilha()
p1.push(10)
p1.push(20)
print(p1.pop())  # 20
print(len(p1))   # 1