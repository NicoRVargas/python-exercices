from time import sleep
gols = []
total = 0
opcao = "S"
jogadores = []
listagols = []
listapartidas = []

while opcao != "N":
    print(40 * "-")

    jogador = {'nome': input("Nome do jogador: ").capitalize(),
               'partidas': int(input("Quantas partidas ele jogou: "))}
    listapartidas.append(jogador['partidas'])
    for c in range(0, jogador['partidas']):
        gol = int(input(f"Quantos gols ele fez na {c+1}° partida: "))
        gols.append([gol])
        total += gol
        listagols = gols[:]

    opcao = input("Deseja continuar[S/N]: ").upper()
    while opcao != "S" and opcao != "N":
        opcao = input("Opção inválida tente novamente. [S/N]: ").upper()

    jogador['ngols'] = gols[:]
    jogador['totgols'] = total
    jogadores.append(jogador)
    total = 0
    gols.clear()

print(25 * "=-")
print(f"{'Jogadores' :^50}")
print(25 * "=-")

print(f"{'No°':<}  {'Nome':<} {'Gols':^37} {'Total':>}")
for c in range(0, len(jogadores)):
    print(f"{c} {jogadores[c]['nome']} {jogadores[c]['ngols']!s:^37} {jogadores[c]['totgols']!s:<50}")

sleep(1.5)

while opcao != 999:
    opcao = int(input("Qual jogador você quer ver detalhes [999]: "))
    while opcao != 999 and opcao >= len(jogadores) or opcao < 0:
        print("Lembrando. Para sair digite [999].")
        opcao = int(input("Não entendi. Qual aluno você quer ver a nota [999]: "))

    if opcao != 999:
        print(25 * "=-")
        print(f"{'Levantamento de'} {jogadores[opcao]['nome']}")
        print(25 * "=-")
        for i, g in enumerate(jogadores[opcao]['ngols']):
            print(f"No jogo {[i+1]} fez: {g} gols")
