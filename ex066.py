num = soma = c = 0
while True:
    num = int(input("Digite um número, insira [999] para sair: "))
    if num == 999:
        break
    soma += num
    c += 1

print(f"Foi digitado {c} números, cujo a soma é {soma}")