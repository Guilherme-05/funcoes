def formatar_dinheiro_PraReal(valor):
    texto = f"R$ {valor:,.2f}" # Padrão EUA 1,200.40
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return texto

preco = float(input("Informe o valor: "))
print(formatar_dinheiro_PraReal(preco))