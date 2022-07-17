opcao = "S"
c = 0
soma = 0
maior_valor = 0
menor_valor = 0
media = 0

while opcao == "S":
    num = int(input("Digite um valor: "))
    opcao = input("Deseja continuar[S/N]? ").upper()
    soma += num
    c += 1
    media = soma/c
    if c == 1:
        maior_valor = menor_valor = num
    else:
        if num > maior_valor:
            maior_valor = num
        if num < menor_valor:
            menor_valor = num

print(f"""Você digitou {c} números.
A média desses valores é {media}, o maior valor é {maior_valor} e o menor {menor_valor}""")

