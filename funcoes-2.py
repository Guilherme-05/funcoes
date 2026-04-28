# Parâmetros com valor padrão (default):
def saudacao(nome, mensagem="Bem vindo!"):
    print(f"Olá {nome}! {mensagem}")

saudacao("Guilherme")
saudacao("Wederson", "Boa noite!")

#Argumentos nomeados (keyword args):
def criar_usuario(nome, idade, admin = False):
    print(f"{nome} | {idade} Anos | Admin = {admin}")

criar_usuario(idade=20, nome="Guilherme")
criar_usuario("Wederson", 45, admin = True)