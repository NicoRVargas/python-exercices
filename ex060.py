num = int(input("Digite um valor: "))
cont = num
fatorial = 1
while cont > 0:
    print(cont, end=" x " if cont != 1 else " = ")
    fatorial *= cont
    cont -= 1

print(f"{fatorial}")





