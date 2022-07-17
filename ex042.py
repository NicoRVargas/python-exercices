lado1n = int(input("insira uma medida: "))
lado2n = int(input("insira uma segunda medida: "))
lado3n = int(input("insira a última medida: "))

if (lado1n - lado2n)**2 **1/2 < lado3n < (lado1n + lado2n):
    if lado1n == lado2n == lado3n:
        print("Esse é um triângulo equilátero.")
    elif lado1n ==lado2n != lado3n or lado1n == lado3n != lado2n or lado2n == lado3n != lado1n:
        print("Esse é um triângulo isóceles.")
    elif lado1n != lado2n != lado3n:
        print("Esse é um triângulo escaleno.")
else:
    print("os valores digitados não formam um triângulo.")



