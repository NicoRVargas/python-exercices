import random
from operator import itemgetter
from time import sleep


jogadores = {'jogador1': random.randint(1, 6),
             'jogador2': random.randint(1, 6),
             'jogador3': random.randint(1, 6),
             'jogador4': random.randint(1, 6),
             'jogador5': random.randint(1, 6)}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
'''sorted do dicionário, key itemgetter(1) pra pegar os valores, reverse pois ele puxa em ordem crescente e eu quero
na descrescente'''

for k, v in jogadores.items():
    print(f"{k} tirou: {v}")
    sleep(0.5)

print(25 * "=")
print("RANKING")
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}.")
    sleep(0.5)
