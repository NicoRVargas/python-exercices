import math
angulo = int(input('Digite o valor do ângulo desejado: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno de {angulo} é {seno:.2f}, o cosseno {cosseno:.2f} e sua tangente {tangente:.2f}')