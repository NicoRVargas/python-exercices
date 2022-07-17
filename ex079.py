valores = []
cont = 0
valoresU = []
while True:
    valores.append(int(input("Digite um valor: ")))
    valoresU = valores[:]
    valoresU.pop()
    if valores[-1] in valoresU:
        valores.pop()
        print("Valor já existente, não computado.")
    opcao = input("Deseja continuar [S/N]: ").upper()
    if opcao == "N".upper():
        valores.sort()
        break
    valores.sort()

print(valores)

