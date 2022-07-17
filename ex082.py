lista = []
listap = []
listai = []
while True:
    lista.append(int(input("Digite um número: ")))
    num = lista[-1]
    if num % 2 == 0:
        listap.append(num)
    if num % 2 != 0:
        listai.append(num)
    opcao = input("Deseja continuar [S/N]: ").upper()
    if opcao == "N".upper():
        break
    if opcao == "S".upper():
        continue
    else:
        opcao = input("Não entendi, deseja continuar [S/N]: ").upper()

print(lista)
print(listap)
print(listai)
