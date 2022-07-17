num = int(input("Digite um número: "))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[32m", end="")
        cont += 1
    else:
        print("\033[31m", end="")
    print(f"{c}", end="")
print(f"\n\033[mO número foi divísivel {cont} vezes.")
if cont == 2:
    print("Por isso, ele é um número primo.")
else:
    print("Então, não é um número primo.")

