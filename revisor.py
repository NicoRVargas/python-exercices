from random import randint
from time import sleep

nome = input('Qual o seu nome: ').strip().capitalize()

print(f'\nTudo bem {nome}? Vou escolher um exercício para você revisar.')
input('Digite enter para que eu procure o exercício.')
while True:

    exercicio = randint(1, 107)

    print('\33[31mEscolhendo\033[m', end='')
    for a in range(0, 6):
        print('\33[31m.\33[m', end='')
        sleep(0.5)
    print(f'\nVocê deve revisar o exercício {exercicio}!!!')

    b = str(input('Já revisou esse a pouco tempo? Aperte \33[1;31m[Enter]\33[m que escolho outro para você'))
    if b == '':
        pass
    else:
        break