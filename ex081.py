lista = []

while True:
    lista.append(int(input("Digite um número: ")))
    opcao = input("Deseja continuar [S/N]: ").upper()
    if opcao == "N".upper():
        break
    if opcao == "S".upper():
        continue
    else:
        opcao = input("Não entendi, deseja continuar [S/N]: ").upper()
print(f"essa lista tem {len(lista)} números.")
lista.sort(reverse=True)
print(f"Ordem decrescente: {lista}")
if 5 in lista:
    print(f"Tem 5 na lista. na posição {lista.index(5)+1}")
if 5 not in lista:
    print("Não tem 5 na lista")