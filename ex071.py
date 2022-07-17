from decimal import Decimal

c50 = c20 = c10 = c1 = c5 = c05 = c025 = c010 = c005 = c001 = 0
print(36*"=")
print("          BANCO DO SHARPÃO")
print(36*"=")
dinheiro = float(input("Qual valor você deseja sacar: R$"))
while dinheiro > 0:
    if dinheiro >= 50:
        dinheiro -= 50
        c50 += 1
    if 20 <= dinheiro < 50:
        dinheiro -= 20
        c20 += 1
    if 10 <= dinheiro < 20:
        dinheiro -= 10
        c10 += 1
    if 5 <= dinheiro < 10:
        dinheiro -= 5
        c5 += 1
    if 1 <= dinheiro < 5:
        dinheiro -= 1
        c1 += 1
    if 0.5 <= dinheiro < 1:
        dinheiro -= 0.5
        c05 += 1
    if 0.25 <= dinheiro < 0.5:
        dinheiro -= 0.25
        c025 += 1
    if 0.10 <= dinheiro < 0.25:
        dinheiro -= 0.10
        c010 += 1
    if Decimal(0.05) <= dinheiro < 0.10:
        dinheiro -= Decimal(0.05)
        c005 += 1
    if Decimal(0.01) <= dinheiro < Decimal(0.05):
        dinheiro -= Decimal(0.01)
        c001 += 1

print(36*"=")
print(f"Você terá {c50} notas de R$50.00")
print(f"Você terá {c20} notas de R$20.00")
print(f"Você terá {c10} notas de R$10.00")
print(f"Você terá {c5} notas de R$5.00")
print(f"Você terá {c1} moedas de R$1.00")
print(f"Você terá {c05} moedas de R$0.50")
print(f"Você terá {c025} moedas de R$0.25")
print(f"Você terá {c010} moedas de R$0.10")
print(f"Você terá {c005} moedas de R$0.05")
print(f"Você terá {c001} moedas de R$0.01")
print(36*"=")
