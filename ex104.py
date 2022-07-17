def leiaint(num):
    while True:
        n = input(num)
        if n.isnumeric() is False:
            print('\033[1;3;31mERROR! Digite um numero inteiro válido.\033[m')
        else:
            return n


number = leiaint(f'{"=-"*20}=\ndigite um numero: ')
print(f'Você acabou de digitar o numero {number}.')
