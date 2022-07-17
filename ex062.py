num = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
c = 1
n = 11

while c < n:
    print(num)
    num += razao
    c += 1
    if c == n:
        termos = int(input("Quantos termos a mais? Digite 0 para sair: "))
        n += termos