info_login = {"username": "yhagodev", "password": "dev225"}

input_username = str(input("Insira seu username:"))
input_password = str(input("Insira sua senha:"))

try:

    if input_username == "" and input_password == "":
        raise ValueError("A entrada não pode ser vazia")

    if input_username == info_login["username"] and input_password == info_login["password"]:
        print("Acesso permitido\n Seja bem vindo ao sistema")
    else:
        print("Credenciais inválidas")

except ValueError as e:
    print(f"Erro: {e}")