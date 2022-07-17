import random
num_aleatorio = random.randint(1,11)
escolha = int(input("Escolha um número de 1 a 10, vamos brincar de adivinhação: "))
cont = 1

while num_aleatorio != escolha:
    escolha = int(input("Escolha errada, tente novamente: "))
    cont += 1
print(f"Parabéns! Você acertou o número {escolha}, você precisou de {cont} palpites para acertar!")