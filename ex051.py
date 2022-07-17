termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razão da P.A: "))

print(25 * "=-")
for c in range(0,10):
    print(f"O termo número {c} é:"f"{termo+(razao*c):^50}")
print(25* "=-")