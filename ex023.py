numero = int(input('Digite um valor inteiro de 0 a 9999: '))

milhar = str(numero // 1000)
centena = str(numero // 100)
dezena = str(numero // 10)
unidade = str(numero // 1)

molde = [milhar[len(milhar) - 1], centena[len(centena) - 1], dezena[len(dezena) - 1], unidade[len(unidade) - 1]]

print(f'Unidade: {molde[3]} \nDezena: {molde[2]} \nCentena: {molde[1]} \nMilhar: {molde[0]}')