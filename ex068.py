import random
c = soma = jogada = opcao = 0
print("Ei! Vamos jogar par ou ímpar! ")
while True:
    pc_jogada = random.randint(1, 2)
    opcao = input("Você quer par ou ímpar [P/I]: ").upper()
    jogada = int(input("Faça sua jogada: "))
    soma = pc_jogada + jogada
    if opcao == "I".upper():
        if soma % 2 == 0:
            print(f"HA! Você perdeu, eu joguei {pc_jogada} e você jogou {jogada}, dando {soma}, um par!")
            break
        else:
            print(f"Droga, eu perdi, eu joguei {pc_jogada} e você jogou {jogada}, dando {soma}, vamos novamente >:(")
    if opcao == "P".upper():
        if soma % 2 == 0:
            print(f"Droga, eu perdi, eu joguei {pc_jogada} e você jogou {jogada}, dando {soma}, vamos novamente >:(")
        else:
            print(f"HA! Você perdeu, eu joguei {pc_jogada} e você jogou {jogada}, dando {soma}, um par!")
            break
    c += 1

print(f"Grande jogo, tivemos {c} partidas até você ganhar.")