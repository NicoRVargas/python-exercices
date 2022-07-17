nome = str(input("Digite seu nome completo: ")) .strip()
print('Ok, irei fazer umasa afirmações sobre seu nome...')

print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsuculo é {nome.lower()}')
print(f'O seu nome tem {len(nome)-nome.count(" ")} letras.')
pnome = nome.split()
print(f'O seu primeiro nome é {pnome[0]} e tem {len(pnome[0])} letras.')
