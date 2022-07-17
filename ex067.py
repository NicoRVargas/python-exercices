num = 0
c = 1
while True:
    num = int(input("Digite um número, Valores negativos encerram o programa: "))
    if num < 0:
        break
    print(16 * "=")
    while c <=10:
        print(f"{num} x {c} = {num*c}")
        c += 1
    print(16 * "=")
    c = 1
print("Programa encerrado.")