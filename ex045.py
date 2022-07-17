import random
print("Vamos jogar jokenpô, escolha sua jogada.")
jogadas = ["pedra", "papel", "tesoura"]
pc_jogada = random.choice(jogadas)

player_jogada = int(input(""""
[1] Pedra
[2] Tesoura   
[3] Papel

Escolha sua jogada: """))

if pc_jogada == "pedra":
    if player_jogada == 1:
        print("Empate.")
    elif player_jogada == 2:
        print("Você perdeu :(")
    elif player_jogada ==3:
        print("Você ganhou, parabéns :)")
elif pc_jogada == "papel":
    if player_jogada == 1:
        print("Você perdeu :(")
    elif player_jogada == 2:
        print("Você ganhou, parabéns :)")
    elif player_jogada == 3:
        print("Empate.")
elif pc_jogada == "tesoura":
    if player_jogada == 1:
        print("Você ganhou, parabéns :)")
    elif player_jogada == 2:
        print("Empate.")
    elif player_jogada == 3:
        print("Você perdeu :(")

