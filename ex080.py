maior = menor = 0
valores = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if n in valores:
        while n in valores:
            n = int(input('Valor duplicado, não vamos adicionar. Digite outro número: '))
            if n not in valores:
                break
    if c == 0:
        maior = menor = n
        valores.append(n)
        print('Valor adicionado na posição 0')
    elif n > maior and not c == 0 and n not in valores:
        maior = n
        valores.append(n)
        print('Valor adicionado na última posição')
    if n < menor and not c == 0:
        menor = n
        valores.insert(0, n)
        print('Valor adicionado na primeira posição')
    if n not in valores:
        for i, v in enumerate(valores):
            if v > n:
                valores.insert(i, n)
                print(f'Valor adicionado na posição {i}')
                break
print(f'A lista formada é {valores}')
