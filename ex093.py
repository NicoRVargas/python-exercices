jogador = {'nome': input("Nome do jogador: "),
           'partidas': int(input("Quantas partidas ele jogou: "))}
gols = []
total = 0

for c in range(0, jogador['partidas']):
    gol = int(input(f"Quantos gols ele fez na {c+1}° partida: "))
    gols.append(gol)
    total += gol

jogador['ngols'] = gols
jogador['totgols'] = total

print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} jogos.")
for c in range(0, jogador['partidas']):
    print(f"na partida {c+1}, fez {gols[c]} gols.")
print(f"No total, {jogador['nome']} fez {jogador['totgols']} gols.")
