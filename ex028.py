from random import randint
nome = input("Olá, qual seu nome? ")

num = randint(1, 5)

adv = int(input(f"{nome}, Ok, vamos brincar de adivininhação. Vou pensar em um número de 1 a 5, tente adivinhar: " ))


if adv == num:
    print("Droga, você acertou, você é bom nisso parabéns. >:C")
else:
    print("Errou! HA! Eu sabia que eu era o melhor nisso >:P")