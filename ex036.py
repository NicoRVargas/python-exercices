casa = float(input("Insira o valor do imóvel que você quer adquirir: "))
salario = float(input("Agora digite seu salário: "))
ano = int(input("Em quantos anos você pretende quitar este imóvel: "))
prestação = casa / (ano * 12)
limite = (salario / 100 * 30)

if prestação > limite:
    print("Desculpe, não podemos financiar este imóvel para você.")
elif prestação <= limite:
    print("Seu empréstimo foi aprovado! Dentro de alguns dias o dinheiro estará na sua conta.")