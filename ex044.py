import time
print("Escolha seu jogo: ")
valor = 0
opcao = int(input("""
[1] Hollow Knight
[2] Dark Souls III
[3] The Legend of Zelda Ocarina of Time

Resposta: """))
if opcao == 1:
    valor = float(27.99)
    print("O jogo escolhido foi Hollow Knight! Excelente escolha.")

elif opcao == 2:
    valor = float(159.90)
    print("O jogo escolhido foi Dark Souls III! Desafiador!")

elif opcao == 3:
    valor = float(99.65)
    print("O jogo escolhido foi The Legend of Zelda Ocarina of Time! Um clássico!")

time.sleep(2)

print(f"O valor do jogo é de R${valor:.2f}. Mas pode variar pela forma de pagamento.")

print("Escolha sua forma de pagamento")
forma_pagamento = int(input("""
    [1] Dinheiro/Cheque
    [2] Cartão à vista
    [3] Cartão até às 2x
    [4] Cartão mais de 3x
    
Resposta: """))

if forma_pagamento == 1:
    print(f"O valor total feito por esta forma de pagamento será de R${valor*0.9:.2f}.")
elif forma_pagamento == 2:
    print(f"O valor total feito por esta forma de pagamento será de R${valor*0.95:.2f}.")
elif forma_pagamento == 3:
    print(f"O valor total feito por esta forma de pagamento será de R${valor:.2f}.")
elif forma_pagamento == 4:
    parcelas = int(input("Digite em quantas vezes você quer parcelar(Max 12): "))
    valor = valor*1.2
    print(f"O valor total feito por esta forma de pagamento será de R${valor:.2f}\n"
    f"Cada parcela terá o valor de R${valor/parcelas:.2f}.")

