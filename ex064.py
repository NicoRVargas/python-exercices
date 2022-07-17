soma = 0
opcao = 0
soma_final = 0
c = 0
while opcao != 999:
    num = int(input("Digite um número, para parar digite [999]: "))
    opcao = num
    soma = num + soma
    soma_final = soma - 999
    c += 1
print(f"A soma dos números digitados é {soma_final} e você digitou {c-1} números no total")