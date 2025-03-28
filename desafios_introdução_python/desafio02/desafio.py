lista_padrao = [3, 8, 12, 5, 6]

lista_pares = [i for i in lista_padrao if i % 2 == 0]
lista_impares = [i for i in lista_padrao if i % 2 != 0]

print(f"Pares: {lista_pares}, Ímpares: {lista_impares}")
