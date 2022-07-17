matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista_pares = []
resultado_pares = 0
lista_terceira_coluna = []
resultado_terceira_coluna = 0
maior_valor = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor para {[l,c]}: "))
        if matriz[l][c] % 2 == 0:
            lista_pares.append(matriz[l][c])
        if matriz[l][2]:
            lista_terceira_coluna.append(matriz[l][2])
        if matriz[1][c] > maior_valor:
            maior_valor = matriz[1][c]
print(12*"=-")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{matriz[l][c]:^5}", end=" ")
    print()

for par in lista_pares:
    resultado_pares += par

for num in lista_terceira_coluna:
    resultado_terceira_coluna += num

print(12*"=-")
print(f"O resultado da soma dos pares da matriz é {resultado_pares}")
print(24* "-")
print(f"A soma da terceira coluna da matriz é {resultado_terceira_coluna}")
print(24* "-")
print(f"O maior valor da segunda linha é {maior_valor}")
print(12*"=-")