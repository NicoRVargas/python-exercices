valores = tuple(int(input('Digite um valor: '))for c in range(1, 5))


print(f"Os números digitados foram {valores}.")
if 9 in valores:
    print(f"Você digitou o número 9 {valores.count(9)} .")
if 9 not in valores:
    print("Você não digitou nenhuma vez o número 9.")
if 3 in valores:
    print(f"O número 3 foi digitado pela primeira vez na posição {valores.index(3)+1}")
if 3 not in valores:
    print("O número 3 não foi digitado nenhuma vez.")

print({n for n in valores if n % 2 == 0}, end=' ')


