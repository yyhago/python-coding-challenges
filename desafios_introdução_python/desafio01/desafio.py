while True:

    primeira_nota = float(input("Digite a sua primeira nota:"))
    segunda_nota = float(input("Digite a sua segunda nota:"))
    terceira_nota = float(input("Digite a sua terceira nota:"))

    if primeira_nota < 0 or primeira_nota > 10 and segunda_nota < 0 or segunda_nota > 10 and terceira_nota < 0 or terceira_nota > 10:
        print("Operação inválida, insira números dentre 0 - 10")
        continue

    media = float((primeira_nota + segunda_nota + terceira_nota) / 3)

    if media >= 7:
        print("Aluno Aprovado!")
    else:
        print("Aluno Reprovado")

    print(f"A média do aluno é: {media:.2f}")
    break