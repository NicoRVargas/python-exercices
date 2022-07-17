num = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
c = 0

print(15 * "=")
while c < 10:
    print(f"o termo {c+1} é {num + (razao*c)}")
    print(15 * "=")
    c += 1

