import math
num1 = float(input('Digite o cateto oposto: '))
num2 = float(input('Difite o cateto adjacente: '))
num3 = (num1 ** 2 + num2 ** 2)

print(f'A hipotenusa do triângulo retângulo de catetos {num1} e {num2} é {math.sqrt(num3):.2f}')


