# # Parâmetros com valor padrão (default):
# def saudacao(nome, mensagem="Bem vindo!"):
#     print(f"Olá {nome}! {mensagem}")

# saudacao("Guilherme")
# saudacao("Wederson", "Boa noite!")

# #Argumentos nomeados (keyword args):
# def criar_usuario(nome, idade, admin = False):
#     print(f"{nome} | {idade} Anos | Admin = {admin}")

# criar_usuario(idade=20, nome="Guilherme")
# criar_usuario("Wederson", 45, admin = True)

# def criar_perfil (nome, idade, cidade):
#     print(f"{nome} | {idade} Anos | {cidade}")

# criar_perfil("Guilherme", 20, "Curitiba")

# def somar_tudo(*numeros):
#     return sum(numeros)

# print(somar_tudo(1, 2))
# print(somar_tudo(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(somar_tudo(10, 20, 30))

# Criando um dicionario

# produto = {"nome": "Teclado", "preco": 150, "em_estoque": True}

# print(produto["nome"])
# produto["preco"] = 135.00
# produto["estoque"] = 24
