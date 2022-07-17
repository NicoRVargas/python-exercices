import random
numeros = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
menor_valor = maior_valor = c = 0
while c <= 4:
    if c == 0:
        menor_valor = maior_valor = numeros[0]
    if numeros[c] > maior_valor:
        maior_valor = numeros[c]
    if numeros[c] < menor_valor:
        menor_valor = numeros[c]
    c += 1

print(numeros)
print(maior_valor)
print(menor_valor)
