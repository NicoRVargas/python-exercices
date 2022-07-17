pesos = []
for i in range(1,6):
    peso = float(input(f"Qual o peso da {i}ª pessoa? "))
    pesos += [peso]
pesos.sort()
print(f'O maior peso lido foi de {pesos[4]} Kg e o menor peso foi de {pesos[0]}')
