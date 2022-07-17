from datetime import date
from math import sqrt
print("Qual seu gênero:")
opção = int(input("""
[1] Masculino
[2] Feminino

Resposta: """))
if opção == 1:
    ano = int(input("Insira o ano de seu nascimento: "))
    anoatual = date.today().year
    if anoatual - ano == 18:
        print("Está no ano de se alistar.")
    if anoatual - ano > 18:
        print(f"Já passou do tempo de se alistar em {(anoatual-ano)-18} ano(s).")
    if anoatual - ano < 18:
        print(f"Ainda falta tempo para se alistar, {18-(anoatual-ano)} ano(s).")
if opção == 2:
    print("Você não precisa se alistar, tenha um bom dia.")



