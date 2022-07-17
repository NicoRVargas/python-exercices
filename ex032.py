"""ano = int(input("Digite um ano: "))
contador = 0
if ano % 4 != 0:
    contador += 1

if ano % 100 == 0 and ano % 400 != 0:
    contador += 1

if contador > 0:
    print("Este não é um ano bissexto.")
else:
    print("Este é um ano bissexto.")"""

#Duas formas pica mlk vamo de pagode q a prada é loucaaaaaaaaaaaaaaaaa

ano = int(input("Insira um ano: "))
ano1 = ano % 4
ano2 = ano % 100
ano3 = ano % 400

if ano1 == 0 and ano2 != 0:
    print("Esse é um ano bissexto.")
elif ano1 == 0 and ano2 == 0 and ano3 == 0:
    print("Esse é um ano bissexto.")
else:
    print("Esse não é um ano bissexto.")





