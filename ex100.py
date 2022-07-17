from random import randint
from time import sleep

lista = []
num = 0


def sorteio():
    for i in range(0, 5):
        num = randint(1, 10)
        print(num, end=" ")
        sleep(0.5)
        lista.append(num)
    print(f"\n{lista}")


def somarpar():
    pares = 0
    for numero in range(0, len(lista)):
        if lista[numero] % 2 == 0:
            pares += lista[numero]
    print(f"A soma dos pares dessa lista é {pares}")


sorteio()
somarpar()
