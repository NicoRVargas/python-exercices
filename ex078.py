valores = []
for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
valores.sort()
print(f"O menor valor é {valores[0]} e o maior {valores[-1]}")
