valores_impares = []
valores_pares = []
valores = []
c = 1

while c <= 7:
    valores.append(int(input(f"Digite o {c}o valor: ")))
    if valores[-1] % 2 == 0:
        valores_pares.append(valores[-1])
    if valores[-1] % 2 != 0:
        valores_impares.append(valores[-1])
    c += 1

valores_pares.sort()
valores_impares.sort()
valores.sort()

print(f"De pares, você digitou os números {valores_pares}")
print(f"Já de ímpares, você digitou os números {valores_impares}")
print(f"E essa é a lista total {valores}")