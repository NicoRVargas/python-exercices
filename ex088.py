import random
palpites = []
jogos = int(input("Digite o número de jogos que você quer fazer: "))
c = 0
c1 = 0

for c in range(0, jogos):
    while c1 < 6:
        num = (random.randint(0, 60))
        if num in palpites:
            c1 -= 1
        if num not in palpites:
            palpites.append(num)
            c1 += 1
    c += 1
    c1 = 0
    print(palpites)
    palpites.clear()


