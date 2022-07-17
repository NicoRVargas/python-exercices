soma = c = c1000 = produto_barato = 0

print(32*"=")
print(f"         LOJA DO NIKOLA")
print(32*"=")
while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    soma += preco
    opcao = input("Deseja continuar [S/N]: ").upper()
    while opcao not in "SN":
        opcao = input("Desculpe, não entendi. Deseja continuar [S/N]: ").upper()
    if c == 0:
        produto_barato = preco
        nome_barato = produto
    if preco < produto_barato:
        produto_barato = preco
        nome_barato = produto
    if preco > 1000:
        c1000 += 1
    c += 1
    if opcao == "N":
        break

print(32*"=")
print(f"""O valor total da compra é R${soma:.2f}
O produto mais barato do carrinho foi {nome_barato.capitalize()}
Teve {c1000} produtos que ultrapassaram R$1000""")