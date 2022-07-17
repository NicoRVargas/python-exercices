num = int(input("Digite um número inteiro a ser convertido: "))

print("""[1] Binário
[2] Hexadecimal
[3] Octadecimal """)
opção = int(input("Digite sua opção: "))

if opção == 1:
    print(f"{num} em binário é {num:b}")
elif opção == 2:
    print(f"{num} em hexadecimal é {num:x}")
elif opção == 3:
    print(f"{num} em octadecimal é {num:o}")
else:
    print("Desculpe, opção inválida.")


