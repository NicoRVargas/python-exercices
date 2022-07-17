num1 = int(input("Digite um número: "))
num2 = int(input("Insira outro número: "))
opção = 0
while opção != 5:
    print("Qual operação gostaria de fazer?")
    print(16*"-=")
    print("""
    [1] Somar.
    [2] Multiplicar.
    [3] Maior.
    [4] Novos números.
    [5] Sair.
    """)
    print(16*"-=")
    opção = int(input(": "))
    if opção == 1:
        print(num1+num2)
    if opção == 2:
        print(num1*num2)
    if opção == 3:
        if num1 > num2:
            print(f"O número {num1} é maior que {num2}")
        if num1 < num2:
            print(f"O número {num2} é maior que {num1}")
        if num1 == num2:
            print("Ambos são iguais.")
    if opção == 4:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Insira outro número: "))
print("Operação finalizada, até mais tarde.")


